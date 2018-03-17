import webbrowser
import os

TEMPLATE_DIR = os.path.abspath(
    os.path.join(os.getcwd(), os.pardir, 'templates')
)
TEMPLATE = os.path.join(TEMPLATE_DIR, 'demo.html')


def open_geojson_in_webbrowser(
    geojson,
    template=TEMPLATE,
    template_dir=TEMPLATE_DIR
):
    with open(template, "r") as f:
        template_html = f.read()
    template_html = template_html.replace(
        "*<-- GEOJSON HERE -->*",
        str(geojson)
    )
    temp_file_path = os.path.join(template_dir, 'temp.html')
    temp_file_url = 'file://' + temp_file_path

    with open(temp_file_path, 'w') as f:
        f.write(template_html)
    webbrowser.open(temp_file_url)
    return geojson


if __name__ == '__main__':
    geojson_example = [{
        "type": "Feature",
        "properties": {
            "party": "Republican",
            "color": "#ff0000"
        },
        "geometry": {
            "type": "Polygon",
            "coordinates": [[
                [-104.05, 48.99],
                [-97.22, 48.98],
                [-96.58, 45.94],
                [-104.03, 45.94],
                [-104.05, 48.99]
            ]]
        }
    }, {
        "type": "Feature",
        "properties": {
            "party": "Democrat",
            "color": "#0000ff"
        },
        "geometry": {
            "type": "Polygon",
            "coordinates": [[
                [-109.05, 41.00],
                [-102.06, 40.99],
                [-102.03, 36.99],
                [-109.04, 36.99],
                [-109.05, 41.00]
            ]]
        }
    }]

    open_geojson_in_webbrowser(geojson_example)
