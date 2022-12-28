from selenium.webdriver.common.by import By

from nicegui import ui

from .screen import Screen


def get_series_0(selenium):
    return selenium.find_elements(By.CSS_SELECTOR, '.highcharts-series-0 .highcharts-point')


def test_change_chart_series(screen: Screen):
    chart = ui.chart({
        'title': False,
        'chart': {'type': 'bar'},
        'xAxis': {'categories': ['A', 'B']},
        'series': [
            {'name': 'Alpha', 'data': [0.1, 0.2]},
            {'name': 'Beta', 'data': [0.3, 0.4]},
        ],
    }).classes('w-full h-64')

    def update():
        chart.options['series'][0]['data'][:] = [1, 1]
        chart.update()

    ui.button('Update', on_click=update)

    screen.open('/')
    screen.wait(0.5)
    before = [bar.size['width'] for bar in get_series_0(screen.selenium)]
    screen.click('Update')
    screen.wait(0.5)
    after = [bar.size['width'] for bar in get_series_0(screen.selenium)]
    assert before[0] < after[0]
    assert before[1] < after[1]


def test_adding_chart_series(screen: Screen):
    chart = ui.chart({
        'title': False,
        'chart': {'type': 'bar'},
    }).classes('w-full h-64')

    def update():
        chart.options['xAxis'] = {'categories': ['A', 'B']}
        chart.options['series'] = [
            {'name': 'Alpha', 'data': [0.1, 0.2]},
            {'name': 'Beta', 'data': [0.3, 0.4]},
        ]
        chart.update()

    ui.button('Update', on_click=update)

    screen.open('/')
    screen.click('Update')
    screen.wait(.5)
    assert len(screen.selenium.find_elements(By.CSS_SELECTOR, '.highcharts-point')) == 6


def test_removing_chart_series(screen: Screen):
    chart = ui.chart({
        'title': False,
        'chart': {'type': 'bar'},
        'series': [
            {'name': 'Alpha', 'data': [0.1, 0.2]},
            {'name': 'Beta', 'data': [0.3, 0.4]},
        ],
    }).classes('w-full h-64')

    def update():
        chart.options['xAxis'] = {'categories': ['A', 'B']}
        chart.options['series'] = [
            {'name': 'Alpha', 'data': [0.1, 0.2]},
        ]
        chart.update()

    ui.button('Update', on_click=update)

    screen.open('/')
    screen.click('Update')
    screen.wait(.5)
    assert len(screen.selenium.find_elements(By.CSS_SELECTOR, '.highcharts-point')) == 3
