try:
    from copy import replace
except ImportError:

    def replace(obj, **kwargs):
        return obj._replace(**kwargs)


from pathlib import Path
from typing import Callable, NamedTuple, Self

import sounddevice as sd
from IPython.display import Audio
from torch import Tensor, clamp, randn_like
from torch.nn import functional as F
from torch.utils.data import Dataset
from torchaudio.datasets import SPEECHCOMMANDS
from torchaudio.datasets.speechcommands import FOLDER_IN_ARCHIVE
from tqdm import tqdm

import torchaudio
from torchaudio import functional as AF


class SpeechSample(NamedTuple):
    waveform: Tensor
    sample_rate: int
    label: str
    speaker_id: str
    utterance_number: int

    @property
    def num_channels(self) -> int:
        return self.waveform.size(0)

    @property
    def num_samples(self) -> int:
        return self.waveform.size(1)

    @property
    def num_seconds(self) -> float:
        return self.num_samples / self.sample_rate

    def play(self) -> None:
        sd.play(
            self.waveform.numpy().reshape(-1, self.num_channels),
            self.sample_rate,
            blocking=True,
        )

    def play_widget(self) -> Audio:
        return Audio(
            self.waveform.numpy(), rate=self.sample_rate, autoplay=True
        )

    def save(self, path: str | Path) -> None:
        torchaudio.save(path, self.waveform, self.sample_rate)

    def apply(self, transform: Callable[[Tensor], Tensor]) -> Self:
        return replace(self, waveform=transform(self.waveform))

    def resample(self, sample_rate: int) -> Self:
        return replace(
            self,
            sample_rate=sample_rate,
            waveform=AF.resample(
                self.waveform,
                orig_freq=self.sample_rate,
                new_freq=sample_rate,
            ),
        )

    def pad_trim(self, seconds: int | float) -> Self:
        num_samples = int(self.sample_rate * seconds)
        if self.num_samples > num_samples:
            return replace(self, waveform=self.waveform[:, :num_samples])
        elif self.num_samples < num_samples:
            padding_amount = num_samples - self.num_samples
            return replace(
                self, waveform=F.pad(self.waveform, (0, padding_amount))
            )
        else:
            return self

    def with_gaussian_noise(self, level=0.01) -> Self:
        noise = randn_like(self.waveform) * level
        return replace(self, waveform=clamp(self.waveform + noise, -1.0, 1.0))


class AugmentedSpeechCommands(Dataset):
    def __init__(
        self,
        folder: str | Path | None = None,
        seconds: int | float | None = None,
        noise_level: float = 0.005,
        enable_noise: bool = True,
        transform: Callable[[Tensor], Tensor] | None = None,
    ) -> None:
        if folder:
            self.folder = Path(folder).resolve()
        else:
            self.folder = Path.cwd() / FOLDER_IN_ARCHIVE
        self._raw_dataset = SPEECHCOMMANDS(
            self.folder.parent, folder_in_archive=self.folder.name
        )
        self._noise = noise_level
        self._enable_noise = enable_noise
        self._transform = transform
        self._seconds = seconds

    def __len__(self) -> int:
        return len(self._raw_dataset)

    def __getitem__(self, index: int) -> SpeechSample:
        relative_path, _, *metadata = self._raw_dataset.get_metadata(index)
        absolute_path = self.folder / relative_path
        waveform, sample_rate = torchaudio.load(absolute_path)
        speech_sample = SpeechSample(waveform, sample_rate, *metadata)

        if self._seconds is not None:
            speech_sample = speech_sample.pad_trim(self._seconds)

        if self._enable_noise:
            speech_sample = speech_sample.with_gaussian_noise(self._noise)

        if self._transform:
            speech_sample = speech_sample.apply(self._transform)

        return speech_sample


def bulk_process(
    dataset: SPEECHCOMMANDS,
    output_dir: str | Path,
    sample_rate: int,
    seconds: int | float,
) -> None:
    for index, sample in tqdm(enumerate(dataset), total=len(dataset)):
        speech_sample = SpeechSample(*sample)
        input_path, *_ = dataset.get_metadata(index)
        output_path = Path(output_dir).resolve() / input_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        if speech_sample.sample_rate != sample_rate:
            speech_sample = speech_sample.resample(sample_rate)
        speech_sample = speech_sample.pad_trim(seconds)
        speech_sample.save(output_path)
