from foxhelpers.foxConfig import OmegaParser

config_parser = OmegaParser()
config_parser.parse_args()
print(config_parser.summary())