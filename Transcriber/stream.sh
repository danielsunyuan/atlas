WHISPER_COREML=1 make stream
./stream -m ./models/ggml-base.en.bin -t 8 --step 500 --length 5000