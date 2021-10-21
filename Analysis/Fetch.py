{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ee416c61",
   "metadata": {},
   "source": [
    "# Fetch Data + Clean Data + Define Functions for Analysis:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "292de252",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import lyricsgenius as genius\n",
    "\n",
    "import string\n",
    "\n",
    "import nltk\n",
    "from nltk.tokenize import sent_tokenize, word_tokenize\n",
    "from nltk.corpus import stopwords\n",
    "from nltk.stem import WordNetLemmatizer "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d0a375c9",
   "metadata": {},
   "source": [
    "### Notes:\n",
    "- Creates Pandas DataFrame with information regarding an artist and their music.\n",
    "- \"search\" parameter refers to any search fields used to find information using the Genius API."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "8e772e47",
   "metadata": {},
   "outputs": [],
   "source": [
    "def findMusic(search, token):\n",
    "\n",
    "    genius = genius.Genius(token)\n",
    "    \n",
    "    # Fields:\n",
    "    song = []\n",
    "    album = []\n",
    "    artist = []\n",
    "    year = []\n",
    "    lyrics = []\n",
    "    \n",
    "    artist = genius.search_artist(search, sort = \"popularity\", include_features = False)\n",
    "    \n",
    "    songs = artist.songs\n",
    "    \n",
    "    for i in songs:\n",
    "        song.append(song.title)\n",
    "        album.append(song.album)\n",
    "        artist.append(song.artist)\n",
    "        year.append(song.year)\n",
    "        lyrics.append(song.lyrics)\n",
    "        \n",
    "    music = pd.DataFrame({\n",
    "        \"Song\" : song,\n",
    "        \"Album\" : album,\n",
    "        \"Artist\" : artist,\n",
    "        \"Year\" : year,\n",
    "        \"Lyrics\" : lyrics\n",
    "    })\n",
    "    \n",
    "    return music"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eaf9564c",
   "metadata": {},
   "source": [
    "### Notes:\n",
    "- Cleans/ fixes data by removing [] and fixing any and all irregularities in the song lyrics."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b7ae7500",
   "metadata": {},
   "outputs": [],
   "source": [
    "def fixLyrics(music, l):\n",
    "    \n",
    "    # l -> music[lyrics]\n",
    "    \n",
    "    music[l] = music[l].str.lower()\n",
    "    \n",
    "    # Based on observations made in EDA, will potentially need to add more:\n",
    "    music[l] = music[l].str.replace(\"[\",\"\")\n",
    "    music[l] = music[l].str.replace(\"]\",\"\")\n",
    "    \n",
    "    music[l] = music[l].str.replace(\"Verse 1\",\"\")\n",
    "    music[l] = music[l].str.replace(\"Verse 2\",\"\")\n",
    "    music[l] = music[l].str.replace(\"Verse 3\",\"\")\n",
    "    \n",
    "    music[l] = music[l].str.replace(\"Refrain\",\"\")\n",
    "    music[l] = music[l].str.replace(\"Chorus\",\"\")\n",
    "    music[l] = music[l].str.replace(\"Bridge\",\"\")\n",
    "    music[l] = music[l].str.replace(\"Outro\",\"\")\n",
    "    music[l] = music[l].str.replace(\"Pre-Chorus\",\"\")\n",
    "    music[l] = music[l].str.replace(\"Spoken\",\"\")\n",
    "    \n",
    "    music[l] = music[l].str.replace(\"URLCopyEmbedCopy\",\"\")\n",
    "    music[l] = music[l].str.replace(\"EmbedShare\",\"\")\n",
    "    \n",
    "    return music   "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "203a6288",
   "metadata": {},
   "source": [
    "### Notes:\n",
    "- https://www.nltk.org/api/nltk.tokenize.html\n",
    "- Normalisation of lyrics.\n",
    "- Removal of stopwords.\n",
    "- Lemmatisation of Word Parameters vs Stemming of Word Parameters.\n",
    "- https://stackoverflow.com/questions/1787110/what-is-the-difference-between-lemmatization-vs-stemming"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "2dd89543",
   "metadata": {},
   "outputs": [],
   "source": [
    "def stopwordLyrics(l):\n",
    "    \n",
    "    nltk.download('stopwords')\n",
    "\n",
    "    # \"Valid\" English:\n",
    "    stops = set(stopwords.words('english'))\n",
    "    \n",
    "    stopsRemove = \" \".join([i for i in l.split() if i not in stops]) \n",
    "    \n",
    "    # \"Valid\" Punctuation:\n",
    "    punctuation = set(string.punctuation)\n",
    "    \n",
    "    punctuationRemove = \" \".join(j for j in stopsRemove if j not in punctuation)\n",
    "    \n",
    "    # Lemmatisation:\n",
    "    lemmatise = WordNetLemmatizer()\n",
    "    \n",
    "    # Normalisation:\n",
    "    normalise = \" \".join(lemmatise.lemmatize(k) for k in punctuationRemove.split())\n",
    "    \n",
    "    return normalise"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
