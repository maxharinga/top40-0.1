import sys
sys.path.insert(0, '/home/mharinga/Documents/git-repos/top40-0.1.git/top40-0.1/src/')
import variationStudy

[years, numArtists] = variationStudy.artistVariation(2002,2015)
variationStudy.plt_artistVariation(years, numArtists)
