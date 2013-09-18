#!/usr/bin/env python
# This file is part of Xpra.
# Copyright (C) 2013 Antoine Martin <antoine@devloop.org.uk>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

from tests.xpra.codecs.test_decoder import test_decoder

def test_dec_avcodec():
    print("test_dec_avcodec()")
    from xpra.codecs.dec_avcodec import decoder #@UnresolvedImport
    #data obtained from nvenc:
    hex_data_list = [
         #each frame as hex:
         "000000016764000aac2b44b602010000000168ee3cb00000000165b8047ff25d9b7ad9bd318d3699e92ca0389d7fc4f72df50c3a8c686c1920d4a308016196143e501a3f06896349e34f3b774d2b3d96446544bba457e404220b9d8a50903b551327ae68a77898d4c1bc2ef26827ee605c82010f7e60e3c1da02c9cfa8d72143f9ac58a2ba06b540982a77ba8bf99a19756be0540aeaf41aacfb524952760513a028d2f30f4c2a127807a46183ceed268af89ed378e68c590185c3d42509aca1704c1c598f5da1e4894f18bf6dff56775238bba39ae9f1687ad8897df9656c537818ddc3b39d4a81353345c5acaa8b1ea7b5ec7ec3788e6adffc163fe076cbb651b1826091b00d12e5c944903d2cd51589362250810a65ed407ba00d6e5748fa4c18d4a9115bbf510d3a8d3bb62a0fbf89583353a963a8c368af2f37d628d94bbc7ff0752aaefc",
         "0000000161e0224fba554753549f44a727e4e3b52c4e0edc9208d197d0000146e02e07c1ff5c",
         "0000000161e0424fb425bccdfc5b8671efea0588c8a7347f2d1ec83bdc1575c59688bb725831f1e588fbab51d3ea35c01515f21f9e9d484bb87e6d1cb170bccd6a9911a16d159bce2c9b3f5a5ea89a03ebc0",
         ]
    test_decoder(decoder, 32, 32, "YUV420P", hex_data_list)

    #now with data obtained from enc_x264:
    hex_data_list = [
         "00000001677a000abcb124b420000003002000000651e244c4c00000000168e88c0e4b22c00000010605ffff64dc45e9bde6d948b7962cd820d923eeef78323634202d20636f7265203133302072323238322031646234363231202d20482e3236342f4d5045472d342041564320636f646563202d20436f70796c65667420323030332d32303133202d20687474703a2f2f7777772e766964656f6c616e2e6f72672f783236342e68746d6c202d206f7074696f6e733a2063616261633d31207265663d38206465626c6f636b3d313a303a3020616e616c7973653d3078333a3078313333206d653d756d68207375626d653d39207073793d31207073795f72643d312e30303a302e3030206d697865645f7265663d31206d655f72616e67653d3136206368726f6d615f6d653d31207472656c6c69733d32203878386463743d312063716d3d3020646561647a6f6e653d32312c313120666173745f70736b69703d31206368726f6d615f71705f6f66667365743d2d3220746872656164733d31206c6f6f6b61686561645f746872656164733d3120736c696365645f746872656164733d30206e723d3020646563696d6174653d3120696e7465726c616365643d3020626c757261795f636f6d7061743d3020636f6e73747261696e65645f696e7472613d3020626672616d65733d3020776569676874703d32206b6579696e743d393939393939206b6579696e745f6d696e3d353030303030207363656e656375743d343020696e7472615f726566726573683d302072633d637266206d62747265653d30206372663d34302e322071636f6d703d302e36302071706d696e3d302071706d61783d3639207170737465703d342069705f726174696f3d312e34302061713d313a312e3030008000000165888415fffebcb6934ea518903f97fff097d18f4a472e1c24c9d1aa95cef09244e3ab695e76fb2befe97e509e0b336c2aaab5b5e3067bf0a99fdeca3ba3b8da0dd93ff64417ffefec7d6e3fe117b6dd3b54bff97f594dfb08b99dfff9375b05eff7cc2195f67cc69e2c9a2dff56da8f2cb3d51a21a4c3d98cc0b417130e8e2b54d4c3f0e80c3a9af689fabb5176d2cdc8a0bd95cecfc43da59d1164297a5061152b58fa59d461e1df48ff581ee5b28924ffe5dec2a7fbdaa83ce89a119e007361550e194ae6566ba0c68a1c7a1580260d42f6bb5a97ae17f5ed343caf464c439fd1cb61d85ad7301aa5a507a9433f698f4fb61cd93dc8113c1ac2b692c65db5afd4be2cfd5b03270d50beaedc342f71bb28ff300245c87bbf6812392b9a8934837c7405ab2fe213ccc79aa7710e41adb4ee606e2237166f2f0c499f6709be1b7a90255d81b48a33429e357665a5d1dcd6e0383357dcffd3bba4dc50e3709548a1449f2e0ff61fce8e1ba2317c8b57caaef5e3f9de91419456971cdbf5fa12c5090f5fc73ccd437d51de0eb022095fd28042aa98f67d057ef43d99022d6ffdb083e41e8a38c729b26e3dc7eb5b23a23800c150f8b3077fe4bf43e42e483643f9c724861cbab28f1838db9277342514499ebeca580ce3f1837b26756ef46e85ee20ec415c68c1a6fa41aef72cfcc5c5c23e452115f8051f623be51ee8f6996404216e9781",
         "00000001419a3a7a2404010040110b7fedec7a4b8cfc2fea3f5cde61281e7a06fdfdce6cfb0393",
         "00000001419a57e10c994c216ffb38728693c81e74f5cffd8b159a15bb9effce3d3e2b68dd2ba539fc81ee4e3c67ad62af5412605a7435d77bd46d2a5e46202f",
         ]
    test_decoder(decoder, 32, 32, "YUV420P", hex_data_list)


def main():
    import logging
    import sys
    logging.root.setLevel(logging.INFO)
    logging.root.addHandler(logging.StreamHandler(sys.stdout))
    test_dec_avcodec()


if __name__ == "__main__":
    main()
