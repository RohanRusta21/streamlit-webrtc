# import streamlit as st
# from streamlit_webrtc import webrtc_streamer, WebRtcMode

# class AudioVideoTransformer:
#     def __init__(self):
#         self.remote_audio = None

#     def transform(self, frame):
#         return frame

# def main():
#     st.title("WebRTC Video Conference")

#     # Get user's display name
#     display_name = st.text_input("Enter your display name")

#     # Get room code from user
#     room_code = st.text_input("Enter room code")

#     # Define a dictionary to store users in the room
#     users = {}

#     # Check if display name and room code are provided
#     if display_name and room_code:
#         # Add the user to the dictionary
#         users[display_name] = room_code

#         # Display the list of users in the room
#         st.write("Users in the room:")
#         for user, code in users.items():
#             st.write(f"- {user} (Room code: {code})")

#         # Define WebRTC streamer with the same key for all users in the room
#         webrtc_ctx = webrtc_streamer(
#             key=room_code,
#             mode=WebRtcMode.SENDRECV,
#             rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
#         )

#         # Display video stream
#         if webrtc_ctx.video_receiver:
#             st.write("Remote Video:")
#             st.write(webrtc_ctx.video_receiver)

#         # Chat functionality
#         st.subheader("Chat")
#         chat_input = st.text_input("Enter message:")
#         if st.button("Send"):
#             # Handle sending the message
#             pass

# if __name__ == "__main__":
#     main()
import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

def main():
    st.title("WebRTC Video Conference")

    # Get user's display name
    display_name = st.text_input("Enter your display name")

    # Get room code from user
    room_code = st.text_input("Enter room code")

    # Define a dictionary to store users in the room
    users = {}

    # Check if display name and room code are provided
    if display_name and room_code:
        # Add the user to the dictionary
        users[display_name] = room_code

        # Display the list of users in the room
        st.write("Users in the room:")
        for user, code in users.items():
            st.write(f"- {user} (Room code: {code})")

        # Define WebRTC streamer with the same key for all users in the room
        webrtc_ctx = webrtc_streamer(
            key=room_code,
            mode=WebRtcMode.SENDRECV,
            rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
        )

        # Display video stream
        if webrtc_ctx.video_receiver:
            st.write("Remote Video:")
            st.write(webrtc_ctx.video_receiver)

if __name__ == "__main__":
    main()
