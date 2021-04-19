import os
import sys
import argparse

def renameSeason(season, args):
	files = sorted(os.listdir('.'))
	files.sort(key=len, reverse=False)
	ext = args.ext
	for count, filename in enumerate(files):
		print(filename)
		dst = args.name + ' S{}E{}'.format(season, count+1) + ext
		src = filename

		os.rename(src, dst)

# Function to rename multiple files
def main():
	parser = argparse.ArgumentParser(description='')
	parser.add_argument("--path")
	parser.add_argument("--ext")
	parser.add_argument("--name")
	parser.add_argument("--season", required=False)
	parser.add_argument("--season_name", 
		help="Used to loop over all seasons. Give season name w/o number to use",
		default=None)
	parser.add_argument("--num_seasons", type=int)
	args = parser.parse_args()

	print(args.path)
	print(args.ext)
	path = args.path

	os.chdir(path)
	print(os.getcwd())
	season = args.season

	if not args.season_name:
		renameSeason(season)
	else:
		for i in range(1, args.num_seasons+1):
			os.chdir(args.season_name + str(i))
			renameSeason(i, args)
			os.chdir("../")


if __name__ == '__main__':
	main()