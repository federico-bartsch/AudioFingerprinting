class Match:
    def find_best_match(input_song, database):
        matches_per_song = {}
        for stored_song in database:
            for hash_value in input_song:
                if hash_value in database[stored_song]:
                    if stored_song not in matches_per_song:
                        matches_per_song[stored_song] = []
                    matches_per_song[stored_song].append((hash_value, input_song[hash_value], database[stored_song][hash_value]))
        song_scores = {}
        scores_histogram = []

        for song, matches in matches_per_song.items():
            song_scores_by_offset = {}

            for hash_val, sample_time, source_time in matches:
                time_offset = source_time - sample_time

                if time_offset not in song_scores_by_offset:
                    song_scores_by_offset[time_offset] = 0
                song_scores_by_offset[time_offset] += 1

            max_offset = (0, 0)

            for offset, score in song_scores_by_offset.items():
                if score > max_offset[1]:
                    max_offset = (offset, score)

            song_scores[song] = max_offset
            scores_histogram.append(max_offset[1])

        scores_histogram.sort()

        """
        Uncomment the following code if you want to plot the histogram:
        
        plt.bar(range(len(scores_histogram)), scores_histogram, color='blue', edgecolor='black')
        plt.xlabel('Song')
        plt.ylabel('Matches')
        plt.title('Matches per song')
        plt.grid(True)
        plt.savefig('matches_per_song.png', format='png', bbox_inches='tight')
        plt.show()
        """
        sorted_scores = list(sorted(song_scores.items(), key=lambda x: x[1][1], reverse=True))
        return sorted_scores[0]