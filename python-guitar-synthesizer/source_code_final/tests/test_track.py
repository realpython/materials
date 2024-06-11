from decimal import Decimal

import numpy as np
import pytest
from digitar.temporal import Time
from digitar.track import AudioTrack


@pytest.fixture
def long_chunk():
    return np.random.rand(12345)


@pytest.fixture
def short_chunk():
    return np.random.rand(6789)


def test_create_audio_track():
    track = AudioTrack(44100)
    assert track.sampling_rate == 44100
    assert track.samples.size == 0
    assert track.samples.shape == (0,)
    assert track.samples.dtype == np.float64


def test_get_audio_track_length():
    track = AudioTrack(44100)
    track.samples = np.random.rand(123)
    assert len(track) == 123


def test_get_audio_track_duration():
    track = AudioTrack(44100)
    track.samples = np.random.rand(123)
    assert track.duration == Time(123 / 44100)


def test_add_consecutive_samples_to_audio_track(long_chunk, short_chunk):
    track = AudioTrack(44100)
    track.add(long_chunk)
    track.add(short_chunk)
    assert len(track) == len(long_chunk) + len(short_chunk)
    assert track.duration == Time((len(long_chunk) + len(short_chunk)) / 44100)
    assert (
        track.samples.tolist()
        == np.concatenate([long_chunk, short_chunk]).tolist()
    )


def test_add_samples_at_specific_instant_without_gap(long_chunk, short_chunk):
    track = AudioTrack(44100)
    track.add_at(Time(seconds=0), long_chunk)
    track.add_at(Time(len(long_chunk) / 44100), short_chunk)
    assert track.samples.size == len(long_chunk) + len(short_chunk)
    assert (
        track.samples.tolist()
        == np.concatenate([long_chunk, short_chunk]).tolist()
    )


def test_add_samples_at_specific_instant_with_gap(long_chunk, short_chunk):
    gap = Time(0.33)
    gap_length = gap.get_num_samples(44100)
    instant = Time(len(long_chunk) / 44100) + gap

    track = AudioTrack(44100)
    track.add(long_chunk)
    track.add_at(instant, short_chunk)

    assert track.samples.size == len(long_chunk) + gap_length + len(
        short_chunk
    )
    assert track.duration == Time(
        (len(long_chunk) + gap_length + len(short_chunk)) / 44100
    )
    assert track.samples[: len(long_chunk)].tolist() == long_chunk.tolist()
    assert (
        track.samples[len(long_chunk) : len(long_chunk) + gap_length].tolist()
        == np.zeros(gap_length).tolist()
    )
    assert (
        track.samples[len(long_chunk) + gap_length :].tolist()
        == short_chunk.tolist()
    )


def test_add_samples_at_specific_instant_with_full_overlap(
    long_chunk, short_chunk
):
    instant = Time(seconds=0.1)
    instant_offset = instant.get_num_samples(44100)

    track = AudioTrack(44100)
    track.add(long_chunk)
    track.add_at(instant, short_chunk)

    assert track.samples.size == len(long_chunk)
    assert track.duration == Time(len(long_chunk) / 44100)

    j = instant_offset + len(short_chunk)
    assert (
        track.samples[instant_offset:j].tolist()
        == (long_chunk[instant_offset:j] + short_chunk).tolist()
    )
    assert (
        track.samples[:instant_offset].tolist()
        == long_chunk[:instant_offset].tolist()
    )
    assert (
        track.samples[instant_offset + len(short_chunk) :].tolist()
        == long_chunk[instant_offset + len(short_chunk) :].tolist()
    )


def test_add_samples_at_specific_instant_with_partial_overlap(
    long_chunk, short_chunk
):
    overlap = Time(0.1)
    overlap_length = overlap.get_num_samples(44100)
    instant = Time(Decimal(len(long_chunk) / 44100) - overlap.seconds)

    track = AudioTrack(44100)
    track.add(long_chunk)
    track.add_at(instant, short_chunk)

    assert (
        track.samples.size
        == len(long_chunk) + len(short_chunk) - overlap_length
    )
    assert track.duration == Time(
        (len(long_chunk) + len(short_chunk) - overlap_length) / 44100
    )
    assert (
        track.samples[
            len(long_chunk) - overlap_length : len(long_chunk)
        ].tolist()
        == (
            long_chunk[-overlap_length:] + short_chunk[:overlap_length]
        ).tolist()
    )
    assert (
        track.samples[: len(long_chunk) - overlap_length].tolist()
        == long_chunk[:-overlap_length].tolist()
    )
    assert (
        track.samples[len(long_chunk) :].tolist()
        == short_chunk[overlap_length:].tolist()
    )
