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
        color: white;
    }
</style>
'''

MAIL_FORMAT = '''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>

{style}

<body>
    <div class="container">
    <h1>오늘자 MoT</h1>
        <table class="">
            <thead>
                <th>온도</th>
                <th>날씨</th>
                <th>미세먼지</th>
                <th>초미세먼지</th>
                <th>오존</th>
            </thead>
            <tbody>
                <tr>
                    <td>{0}  {1}</td>
                    <td>{2}</td>
                    <td>{3}</td>
                    <td>{4}</td>
                    <td>{5}</td>
            </tbody>
        </table>
        <table>
            <thead>
                <th>헤드라인</th>
            </thead>
            <tbody>
                <tr>
                    <td>{6}</td>
                </tr>
                <tr>
                    <td>{7}</td>
                </tr>
                <tr>
                    <td>{8}</td>
                </tr>
                <tr>
                    <td>{9}</td>
                </tr>
                <tr>
                    <td>{10}</td>
                </tr>
                <tr>
                    <td>{11}</td>
                </tr>
                <tr>
                    <td>{12}</td>
                </tr>
            </tbody>
        </table>
        <table>
            <thead>
                <th>정치</th>
            </thead>
            <tbody>
                <tr>
                    <td>{13}</td>
                </tr>
                <tr>
                    <td>{14}</td>
                </tr>
                <tr>
                    <td>{15}</td>
                </tr>
                <tr>
                    <td>{16}</td>
                </tr>
                <tr>
                    <td>{17}</td>
                </tr>
                <tr>
                    <td>{18}</td>
                </tr>
            </tbody>
        </table>
        <table>
            <thead>
                <th>경제</th>
            </thead>
            <tbody>
                <tr>
                    <td>{19}</td>
                </tr>
                <tr>
                    <td>{20}</td>
                </tr>
                <tr>
                    <td>{21}</td>
                </tr>
                <tr>
                    <td>{22}</td>
                </tr>
                <tr>
                    <td>{23}</td>
                </tr>
                <tr>
                    <td>{24}</td>
                </tr>
            </tbody>
        </table>
        <table>
            <thead>
                <th>사회</th>
            </thead>
            <tbody>
                <tr>
                    <td>{25}</td>
                </tr>
                <tr>
                    <td>{26}</td>
                </tr>
                <tr>
                    <td>{27}</td>
                </tr>
                <tr>
                    <td>{28}</td>
                </tr>
                <tr>
                    <td>{29}</td>
                </tr>
                <tr>
                    <td>{30}</td>
                </tr>
            </tbody>
        </table>
        <table>
            <thead>
                <th>생활/문화</th>
            </thead>
            <tbody>
                <tr>
                    <td>{31}</td>
                </tr>
                <tr>
                    <td>{32}</td>
                </tr>
                <tr>
                    <td>{33}</td>
                </tr>
                <tr>
                    <td>{34}</td>
                </tr>
                <tr>
                    <td>{35}</td>
                </tr>
                <tr>
                    <td>{36}</td>
                </tr>
            </tbody>
        </table>
        <table>
            <thead>
                <th>세계</th>
            </thead>
            <tbody>
                <tr>
                    <td>{37}</td>
                </tr>
                <tr>
                    <td>{38}</td>
                </tr>
                <tr>
                    <td>{39}</td>
                </tr>
                <tr>
                    <td>{40}</td>
                </tr>
                <tr>
                    <td>{41}</td>
                </tr>
                <tr>
                    <td>{42}</td>
                </tr>
            </tbody>
        </table>
        <table>
            <thead>
                <th>IT/과학</th>
            </thead>
            <tbody>
                <tr>
                    <td>{43}</td>
                </tr>
                <tr>
                    <td>{44}</td>
                </tr>
                <tr>
                    <td>{45}</td>
                </tr>
                <tr>
                    <td>{46}</td>
                </tr>
                <tr>
                    <td>{47}</td>
                </tr>
                <tr>
                    <td>{48}</td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
</html>'''
