Now for something a little different. 0x2262c96b is loaded into memory in the main function. Examine byte-wise the memory that the constant is loaded in by using the GDB command x/4xb addr. The flag is the four bytes as they are stored in memory. If you find the bytes 0x11 0x22 0x33 0x44 in the memory location, your flag would be: picoCTF{0x11223344}.

hint1:You'll need to breakpoint the instruction after the memory load.

hint2:Use the gdb command x/4xb addr with the memory location as the address addr to examine. GDB manual page.

hint3:Any registers in addr should be prepended with $ like $rbp.

hint4:Don't use square brackets for addr

hint5:What is endianness?
