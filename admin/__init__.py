import streamlit as st
import streamlit.components.v1 as components


img_path = "admin/static/menu.jpeg"

components.html(
    html="""
    <style>
        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #f5f5f5;
        }
        
        img {
            max-width: 80%;
            cursor: pointer;
            transition: transform 0.3s ease;
        }
        
        img:hover {
            transform: scale(1.02);
        }
        
        .fullscreen {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: contain;
            background-color: rgba(0, 0, 0, 0.9);
            z-index: 1000;
            cursor: zoom-out;
        }
    </style>
    <script>
        function toggleFullScreen(element) {
            if (!document.fullscreenElement) {
                if (element.requestFullscreen) {
                    element.requestFullscreen();
                } else if (element.webkitRequestFullscreen) {
                    element.webkitRequestFullscreen();
                } else if (element.msRequestFullscreen) {
                    element.msRequestFullscreen();
                }
                element.classList.add('fullscreen');
            } else {
                if (document.exitFullscreen) {
                    document.exitFullscreen();
                } else if (document.webkitExitFullscreen) {
                    document.webkitExitFullscreen();
                } else if (document.msExitFullscreen) {
                    document.msExitFullscreen();
                }
                element.classList.remove('fullscreen');
            }
        }

        document.addEventListener('fullscreenchange', function() {
            const img = document.querySelector('img');
            if (!document.fullscreenElement) {
                img.classList.remove('fullscreen');
            }
        });
    </script>
    <div class="image-container">
        <img src="https://kr.object.ncloudstorage.com/signage-bucket/test.jpeg" alt="클릭하여 전체화면" onclick="toggleFullScreen(this)">
    </div>
    """,
    height=400,
)
