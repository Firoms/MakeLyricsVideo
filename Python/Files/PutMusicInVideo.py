import moviepy.editor as mp

audio = mp.AudioFileClip("../../Musics/test.mp3")
video1 = mp.VideoFileClip("../../Videos/test.avi")
final = video1.set_audio(audio)
final.write_videofile("../../Videos/output.mp4",codec= 'mpeg4', audio_codec='libvorbis')