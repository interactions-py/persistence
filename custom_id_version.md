# Custom ID Format Versions

### Legacy
#### Prefix: p~

This is the oldest supported format, created on July 3rd. Any formats from before this have been deemed obsolute. We combined the tag and the package and encrypted them together. The problem with this format is that we chain the encryptions together when longer than 28, but we can only encrypt strings between 4 and 28 characters in length. Therefore, we needed a different approach which would be breaking.

### v1.0.0
#### Prefix p0~

The first version of the formatting system, this changed how encryption and decryption works by encrypting in chains of 24 and expanding the last block to 28 when neccisary. This allows for custom_ids of any length up to 100 without gaps in the middle. However, legacy custom_ids can stil be recieved! This means that this change isn't breaking. New custom_ids automatically use this version, but old ones are still recieved as they should be.