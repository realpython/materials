from meta_classes import EmailReader, PdfReader, VirtualFileReader

print(isinstance(PdfReader(), VirtualFileReader))
print(issubclass(PdfReader, VirtualFileReader))
print(issubclass(EmailReader, VirtualFileReader))
