from nicegui import ui

from . import documentation, example_card, svg
from .examples import examples
from .header import add_head_html, add_header
from .style import example_link, features, heading, link_target, section_heading, subtitle, title


def create_hero_section():
    with ui.row().classes('w-full h-screen items-center justify-center gap-8 pr-4 no-wrap into-section'):
        # Add your logo or image if you have any
        # svg.face(half=True).classes('stroke-black dark:stroke-white w-[200px] md:w-[230px] lg:w-[300px]')
        with ui.column().classes('gap-4 md:gap-8 pt-32 items-center text-center'):
            ui.label('Unlock the Youtube video').classes('text-4xl font-bold text-green-600')
            ui.label('Power of knowhow.ai Today!').classes('text-4xl font-bold text-green-600')
            ui.label('Transform YouTube videos into interactive slides containing charts, tables, key points, and highlights. Knowhow.ai not only supports Summary for YouTube/Video but also offers AI-powered Content and personal blog.').classes('text-lg text-white max-w-lg')
            with ui.row().classes('gap-4 justify-center'):
                # ui.button('Get Started').classes('bg-white text-black')
                # ui.button('Learn More').classes('bg-gray-700 text-white')
                # ui.input('name@email.com').placeholder('Enter your email').classes('mt-4')
                ui.link('Try to Convert Now', '/demo').classes('bg-green-600 text-white px-4 py-2 rounded')

def create_features_section():
    with ui.row().classes('w-full min-h-screen bg-gray-50 py-20 items-center justify-center'):
        with ui.column().classes('max-w-2xl text-left'):
            ui.label('Convert YouTube videos into engaging presentations and Screenshots').classes('text-3xl font-bold text-gray-700')
            ui.label('With knowhow.ai, you can easily transform YouTube videos into visually stunning presentations. Our platform allows you to capture screenshots, create slides with charts and tables, and highlight key takeaways, all with immersive translation capabilities.').classes('text-lg text-gray-700')
            with ui.row().classes('gap-4 mt-8'):
                ui.button('Get Started').classes('bg-black text-white')
                ui.button('Learn More').classes('bg-gray-300 text-black')

def create_user_types_section():
    with ui.row().classes('w-full min-h-screen bg-black text-white py-20'):
        with ui.column().classes('max-w-6xl mx-auto text-center'):
            ui.label('Who Loves Knowhow.ai').classes('text-3xl font-bold')
            ui.label('for Convert Video into Content').classes('text-3xl font-bold text-green-500')
            with ui.row().classes('gap-8 justify-center mt-8'):
                for title, desc in [
                    ('Video and Youtube Creators', 'Learn about hosting built for scale and reliability.'),
                    ('Online learning & Students', 'Learn how Framer can optimize your site for search engines.'),
                    ('Marketing managers & HR team', 'Get inspired by blogs, job openings, events and more.')
                ]:
                    with ui.column().classes('bg-gray-800 p-4 rounded-lg max-w-xs'):
                        ui.image('https://2.bp.blogspot.com/-7TdBxJhuPFM/V_sZCBPcGNI/AAAAAAAApO0/tK3J4YTc3mIkAHrIhm8zpgwA9NT9orIFwCLcB/s1600/2.png').classes('w-full h-auto mb-4')
                        ui.label(title).classes('text-xl font-bold')
                        ui.label(desc).classes('text-lg text-gray-400')
                        ui.button('Read More').classes('bg-black text-white mt-4')



def create_how_it_works_section():
    with ui.row().classes('w-full min-h-screen bg-gray-900 text-white py-20'):
        with ui.column().classes('max-w-6xl mx-auto text-center'):
            ui.label('Watch and Learn every single moment').classes('text-3xl font-bold')
            ui.label('Unlock the Power of YouTube with knowhow.ai').classes('text-lg text-green-500')
            with ui.row().classes('gap-8 justify-center mt-8'):
                for title, desc in [
                    ('How does Knowhow.AI work?', 'Knowhow.AI takes your preferred YouTube video and transforms it into a storyboard. This visual outline gives you a frame-by-frame representation of the video scene progression complemented with instantaneous translations.'),
                    ('Not only Script But Also Keynote Storyboard', 'A storyboard presents your YouTube video as a series of static frames or images, each depicting a specific scene. It’s like having a comic strip version of your video.'),
                    ('Can I customize my YT notes?', 'Absolutely! YouTube notes and Blog isn’t just a converter, it’s a customization wizard! Choose your screenshots, adjust their layout, and select your preferred translations. Your storyboard, your rules!')
                ]:
                    with ui.column().classes('bg-gray-900 p-4 rounded-lg max-w-xs text-left'):
                        ui.label(title).classes('text-xl font-bold')
                        ui.label(desc).classes('text-lg text-green-200')

def create_testimonials_section():
    with ui.row().classes('w-full min-h-screen bg-black text-white py-20'):
        with ui.column().classes('max-w-6xl mx-auto text-center'):
            ui.label('Meet our lover Creator and E-learning').classes('text-3xl font-bold')
            with ui.row().classes('gap-8 justify-center mt-8'):
                testimonials = [
                    ('均一教育平台 CTO, 子揚', 'Transforming my YouTube videos into storyboards and Screenshot was a game-changer!'),
                    ('WeCan, E-Education Founder', 'Knowhow.AI brings my videos to online learning in a whole new way! Not only easy to watch but also to notes taking and review immediately.'),
                    ('Lucy Liu', 'With storyboard translation, my content reaches more people.')
                ]
                for testimonial in testimonials:
                    name, desc = testimonial
                    title = ''  # 设置空标题，防止错误
                    
                    with ui.column().classes('bg-gray-900 p-4 rounded-lg max-w-xs text-left'):
                        ui.image('https://2.bp.blogspot.com/-7TdBxJhuPFM/V_sZCBPcGNI/AAAAAAAApO0/tK3J4YTc3mIkAHrIhm8zpgwA9NT9orIFwCLcB/s1600/2.png').classes('w-full h-auto mb-4')
                        ui.label(desc).classes('text-lg')
                        ui.label(name).classes('text-xl font-bold mt-4')
                        ui.label(title).classes('text-lg text-gray-400')

def create_footer_section():
    with ui.row().classes('w-full bg-white py-8'):
        with ui.column().classes('max-w-4xl mx-auto text-center'):
            ui.label('Join Knowhow Whitelist and get weekly Youtube Summary').classes('text-3xl font-bold')
            ui.button('Join Now').classes('bg-black text-white mt-4')
            ui.label('Copyright © 2024 Knowhow.ai. All Rights Reserved.').classes('text-lg text-gray-500 mt-8')
            ui.label('Generated on Monday, June 3, 2024').classes('text-sm text-gray-400')

def create() -> None:
    """Create the content of the main page."""
    ui.context.client.content.classes('p-0 gap-0')
    add_head_html()
    add_header()

    create_hero_section()
    create_features_section()
    create_user_types_section()
    create_how_it_works_section()
    create_testimonials_section()
    create_footer_section()
