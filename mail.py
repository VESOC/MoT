STYLES = '''
<style>
    body {
        width: 70vw;
        text-align: center;
        color: rgba(96, 173, 141, 0.932);
        background-color: black;
    }

    h1 {
        color: rgb(116, 171, 253);
    }

    .container {
        width: 100%;
        margin: 10px;
    }

    .weather {
        font-size: 20px;
    }
    
    table {
        width: 100%;
        text-align: center;
        border: 2px solid;
        margin-bottom: 15px;
    }
    
    th {
        border-bottom: 1px solid;
        font-size: 16px;
        color: rgb(245, 98, 0);
        background-color: white;
        margin-bottom: 10px;
    }

    td {
        border: 1px solid rgba(32, 229, 255, 0.932);
    }

    a {
        color: white;
        text-decoration: none;
    }
</style>
'''

WEATHER_FORMAT = '''
        <table class="weather">
            <thead>
                <th>온도</th>
                <th>날씨</th>
                <th>미세먼지</th>
                <th>초미세먼지</th>
                <th>오존</th>
            </thead>
            <tbody>
                <td>{}{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tbody>
        </table>
'''

NEWS_TABLE_FORMAT = '''
<table>
    <thead>
        <th>{TYPE}</th>
    </thead>
    <tbody>
{ARTICLES}
    </tbody>
</table>
'''

ARTICLE_FORMAT = '''
        <tr>
            <td><a href="{}" target="_blank">{}</a></td>
        </tr>
'''

MAIL_FORMAT = '''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>

{STYLE}

<body>
    <div class="container">
    <h1>오늘자 MoT</h1>
{WEATHER}
{NEWS}
    </div>
</body>
</html>'''
