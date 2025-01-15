import spotipy
from spotipy.oauth2 import SpotifyOAuth

# data from Spotify Developer
CLIENT_ID = 'your client_id'
CLIENT_SECRET = 'your client_secret'
REDIRECT_URI = 'redirect_url'

# authentication
scope = "user-library-read user-library-modify"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=scope))

# getting all your favourite songs
def get_all_favorite_tracks():
    tracks = []
    results = sp.current_user_saved_tracks(limit=50)
    while results:
        for item in results['items']:
            tracks.append(item['track']['id'])
        if results['next']:
            results = sp.next(results)
        else:
            break
    return tracks

# deleting your tracks by 20
def remove_tracks_in_batches(track_ids):
    batch_size = 20
    for i in range(0, len(track_ids), batch_size):
        batch = track_ids[i:i + batch_size]
        sp.current_user_saved_tracks_delete(tracks=batch)
        print(f"Delleted {len(batch)} tracks.")

# main process
if __name__ == "__main__":
    favorite_tracks = get_all_favorite_tracks()
    print(f"Found {len(favorite_tracks)} trackes in 'Favourite'.")
    
    if favorite_tracks:
        remove_tracks_in_batches(favorite_tracks)
        print("All tracks are deleted from 'Favourite'.")
    else:
        print("List 'Favourite' is empty.")