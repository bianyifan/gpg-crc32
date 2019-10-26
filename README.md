# GPG Key CRC32 Utility

The most secure material to store GPG keys is paper.

Printing is simple, but how to import keys from paper?

## Usage

Export: 

- Export GPG keys;
- Append CRC32 checksum to each line of a file; then
- Print it out, keep it at a safe place.

Import:

- Scan that paper;
- Verify the CRC32 checksum, and remove them, now we have the original file; then
- Import GPG keys.

