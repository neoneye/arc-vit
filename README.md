# arc-vit

I did some unsuccessful experiments myself, where I based my code on an example that with high accuracy 80% could classify if an image is this a dog or a cat. Instead of dog/cat, I made 10 classifications corresponding to the 10 allowed pixel colors. And I ran the entire ViT for every pixel in the predicted output. So many many invocations of the ViT.

I don't have access to a powerful GPU/TPU for training. I think the longest training I did was 7 days on a mac with M1 chip. Training for longer than me on better hardware and it may be better at classifying the pixel colors of the result.

