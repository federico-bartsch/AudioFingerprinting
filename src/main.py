from record import Record
from match import Match
from database import Database
from fingerprintGenerator import FingerprintGenerator
import os
if __name__ == "__main__":
    audio_path = "recorded_audio.wav"
    database_path = "/Users/federico/Desktop/trento/Signal image and video /shazam2/database2.pickle"
    duration_seconds = 2
    sample_rate = 44100

    # Check if the database already exists, if it exist, load the database, otherwise create a new one
    if os.path.exists("database4.pickle"):
        database = Database.load_database(database_path)
    else:
        database = Database.create_database("music")
        Database.save_database(database_path, database)

    # Record audio for 7 seconds
    recorded_data = Record.record_audio(duration_seconds, sample_rate)
    Record.save_audio(audio_path, recorded_data, sample_rate)
    
    
    # Generate the fingerprint of the recorded audio
    input_song = FingerprintGenerator.generate_fingerprint(audio_path)
    # Find the best match by checking for matches in the database
    best_match = Match.find_best_match(input_song, database)
    print(f"The best match is: {best_match}")

