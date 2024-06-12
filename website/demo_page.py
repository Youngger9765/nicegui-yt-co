from nicegui import ui
from gradio_client import Client
import json

def show_loading_spinner():
    ui.run_javascript('document.getElementById("loading_spinner").classList.remove("hidden");')  # Show the loading spinner

def hide_loading_spinner():
    ui.run_javascript('document.getElementById("loading_spinner").classList.add("hidden");')  # Hide the loading spinner

def fetch_and_show_result():
    result_label.text = ''
    youtube_link = youtube_input.value
    if not youtube_link:
        result_label.text = 'Please enter a valid YouTube link.'
        hide_loading_spinner()
        return

    video_id = youtube_link.split('v=')[-1]
    print(f"youtube_link: {youtube_link}")
    print(f"video_id: {video_id}")

    client = Client("AiCloudTW/video_bot_999")
    
    try:
        result = client.predict(
            "6161",  # str  in 'Password' Textbox component
            video_id,  # str  in 'Enter YouTube Link' Textbox component
            "open-ai-gpt-4o",  # Literal[open-ai-gpt-4o, anthropic-claude-3-sonnet]  in 'LLM Model' Dropdown component
            api_name="/process_youtube_link"
        )
        print(f"Raw result: {result}")

        # Extracting result to variables
        video_id = result[0]
        questions_answers_json = result[1]
        original_transcript = result[2]
        summary_text = result[3]
        summary = result[4]
        key_moments_text = result[5]
        key_moments_html = result[6]
        mind_map = result[7]
        mind_map_html = result[8]
        html_content = result[9]
        simple_html_content = result[10]
        reading_passage_text = result[11]
        reading_passage = result[12]
        subject = result[13]
        grade = result[14]

        # Display the result in the front end
        ui.run_javascript(f"showUnicodeResult({json.dumps(result)}, {json.dumps(key_moments_text)})")
        ui.run_javascript(f"showYouTubeVideo('{video_id}')")

    except Exception as e:
        print(f"Prediction error: {e}")
        ui.run_javascript(f"showUnicodeResult('Error: {e}')")
    finally:
        hide_loading_spinner()

def create() -> None:
    global result_label, youtube_input
    with ui.row().style('margin: auto;'):
        youtube_input = ui.input('Enter YouTube Link').props('autogrow').style('width: 500px; margin:auto;')
        ui.button('Try Demo', on_click=lambda: (show_loading_spinner(), ui.timer(1, fetch_and_show_result, once=True)))
    with ui.column().style('margin: auto;'):
        result_label = ui.label('')
        ui.html('''
            <div id="loading_spinner" class="hidden" style="margin:auto">
                <svg width="100" height="100" viewBox="0 0 44 44" xmlns="http://www.w3.org/2000/svg" stroke="#000">
                    <g fill="none" fill-rule="evenodd" stroke-width="2">
                        <circle cx="22" cy="22" r="1">
                            <animate attributeName="r"
                                begin="0s" dur="1.8s"
                                values="1; 20"
                                calcMode="spline"
                                keyTimes="0; 1"
                                keySplines="0.165, 0.84, 0.44, 1"
                                repeatCount="indefinite" />
                            <animate attributeName="stroke-opacity"
                                begin="0s" dur="1.8s"
                                values="1; 0"
                                calcMode="spline"
                                keyTimes="0; 1"
                                keySplines="0.3, 0.61, 0.355, 1"
                                repeatCount="indefinite" />
                        </circle>
                        <circle cx="22" cy="22" r="1">
                            <animate attributeName="r"
                                begin="-0.9s" dur="1.8s"
                                values="1; 20"
                                calcMode="spline"
                                keyTimes="0; 1"
                                keySplines="0.165, 0.84, 0.44, 1"
                                repeatCount="indefinite" />
                            <animate attributeName="stroke-opacity"
                                begin="-0.9s" dur="1.8s"
                                values="1; 0"
                                calcMode="spline"
                                keyTimes="0; 1"
                                keySplines="0.3, 0.61, 0.355, 1"
                                repeatCount="indefinite" />
                        </circle>
                    </g>
                </svg>
            </div>
        ''').style('margin: auto;')
        with ui.row().style('margin: auto;'):
            ui.html('''
                <div id="youtube_video_container" style="margin:auto;">
                    <iframe id="youtube_video" width="560" height="315" src="" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                </div>
            ''').style('margin: auto;')
            ui.html('''
                <div id="result">
                    Result will be shown here.
                </div>
            ''')

    # Embed HTML and JavaScript at the end of the body
    ui.add_body_html('''
        <script>
            function showYouTubeVideo(videoId) {
                const youtubeIframe = document.getElementById('youtube_video');
                youtubeIframe.src = `https://www.youtube.com/embed/${videoId}`;
            }
            function showUnicodeResult(result, key_moments_text) {
                if (typeof key_moments_text === 'string') {
                    key_moments_text = JSON.parse(key_moments_text);
                }

                let resultHtml = '<div style="display: flex; flex-wrap: wrap;">';

                key_moments_text.forEach((moment, index) => {
                    let imagesHtml = '';
                    if (moment.suggested_images && moment.suggested_images.length > 0) {
                        imagesHtml += '<div class="image-gallery" style="position: relative;">';
                        moment.suggested_images.forEach((img, imgIndex) => {
                            imagesHtml += `
                                <img src="${img}" alt="Suggested Image" class="gallery-img" data-index="${imgIndex}" style="display: ${imgIndex === 0 ? 'block' : 'none'}; width: 100%; height: auto;">
                            `;
                        });
                        imagesHtml += `
                            <button class="gallery-prev" onclick="prevImage(${index})" style="position: absolute; left: 0; top: 50%; transform: translateY(-50%); background-color: rgba(0,0,0,0.5); color: white; border: none; cursor: pointer; font-size: 18px; padding: 10px;">&#10094;</button>
                            <button class="gallery-next" onclick="nextImage(${index})" style="position: absolute; right: 0; top: 50%; transform: translateY(-50%); background-color: rgba(0,0,0,0.5); color: white; border: none; cursor: pointer; font-size: 18px; padding: 10px;">&#10095;</button>
                        `;
                        imagesHtml += '</div>';
                    }

                    let keywordsHtml = '';
                    if (moment.keywords && moment.keywords.length > 0) {
                        moment.keywords.forEach(keyword => {
                            keywordsHtml += `<label style="background-color: #eee; border-radius: 3px; padding: 2px 5px; margin: 2px; display: inline-block;">${keyword}</label>`;
                        });
                    }

                    resultHtml += `
                        <div class="storycard" style="border:1px solid #ddd;padding:10px;margin:10px;width:30%;box-sizing: border-box;">
                            <div style="text-align:center;">
                                ${imagesHtml}
                            </div>
                            <div style="margin-top:10px;">
                                <p>${moment.text}</p>
                            </div>
                            <div style="margin-top:10px;">
                                ${keywordsHtml}
                            </div>
                        </div>
                    `;
                });

                resultHtml += '</div>';
                document.getElementById('result').innerHTML = resultHtml;
            }

            function prevImage(galleryIndex) {
                const gallery = document.querySelectorAll('.image-gallery')[galleryIndex];
                const images = gallery.querySelectorAll('.gallery-img');
                const currentIndex = Array.from(images).findIndex(img => img.style.display === 'block');
                images[currentIndex].style.display = 'none';
                const prevIndex = (currentIndex - 1 + images.length) % images.length;
                images[prevIndex].style.display = 'block';
            }

            function nextImage(galleryIndex) {
                const gallery = document.querySelectorAll('.image-gallery')[galleryIndex];
                const images = gallery.querySelectorAll('.gallery-img');
                const currentIndex = Array.from(images).findIndex(img => img.style.display === 'block');
                images[currentIndex].style.display = 'none';
                const nextIndex = (currentIndex + 1) % images.length;
                images[nextIndex].style.display = 'block';
            }
        </script>
    ''')