TOKEN = '' #insert your Telegram bot token here

SRC_vocab_path = './transformer/model_weights/SRC.p'	# source (russian) vocabulary look-up table (torchtext.vocab object)
TRG_vocab_path = './transformer/model_weights/TRG.p'	# target (english) vocabulary look-up table (torchtext.vocab object)

checkpoint_path = './transformer/model_weights/best-val-model_47_epoch.pt'	# model weights which should be downloaded from here
										# https://drive.google.com/file/d/1BY4Lv_KEIGJj3APPO4PLbQ1RWGiJsSm4/view?usp=sharing
																			                                      # https://drive.google.com/file/d/1gj-GJJuLMO87oLQw6xqWgRU9YI3Bed_u/view?usp=sharing
