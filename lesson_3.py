from flask import Flask, render_template
import uuid
import time
import datetime
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_data/<int:num>')
def about(num=3):
    main_list = []
    for i in range(int(num)):
        start_time = time.monotonic()
        start_time_now = datetime.datetime.now()
        start_time_now = start_time_now.strftime('%d-%m-%Y %H:%M:%S')
        uuid_data = uuid.uuid4()
        time.sleep(0.1)
        end_time = time.monotonic()
        request_execution_time = end_time - start_time
        main_list.append({})
        main_list[i]['uuid_data'] = uuid_data
        main_list[i]['start_time_now'] = start_time_now
        main_list[i]['request_execution_time'] = request_execution_time
    return render_template('get_data.html', num=int(num),  main_list=main_list)


if __name__ == '__main__':
    app.run(debug=True)
