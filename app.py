from flask import Flask, render_template, request

app = Flask(__name__)


def get_bmi_category_and_advice(bmi: float) -> tuple:
    if bmi < 18.5:
        category = "體重過輕"
        advice = (
            "考慮增加熱量攝取與規律阻力訓練以增加肌肉量。"
            " 可諮詢營養師以取得個人化飲食建議。"
        )
    elif 18.5 <= bmi < 25:
        category = "正常範圍"
        advice = (
            "維持均衡飲食與規律運動，繼續保持良好生活習慣。"
        )
    elif 25 <= bmi < 30:
        category = "過重"
        advice = (
            "建議調整飲食（降低高熱量食物）、增加有氧與阻力運動。"
            " 若需要，可尋求專業營養師或醫師協助制定計劃。"
        )
    else:
        category = "肥胖"
        advice = (
            "建議儘早與醫療或營養專業人士討論減重計畫，"
            " 包含飲食、運動與可能的醫療介入。"
        )

    # 額外的簡短生活建議
    extra = (
        "建議每週至少150分鐘中等強度有氧運動，"
        " 每週2次以上阻力訓練；保持充足睡眠與減少菸酒。"
    )

    return category, advice + "\n" + extra


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        weight = request.form.get('weight', '').strip()
        height = request.form.get('height', '').strip()

        error = None
        try:
            weight_val = float(weight)
            height_val = float(height)
            if height_val > 3:  # assume user entered cm
                height_m = height_val / 100.0
            else:
                height_m = height_val

            if weight_val <= 0 or height_m <= 0:
                error = '請輸入大於 0 的身高與體重。'
            else:
                bmi = weight_val / (height_m ** 2)
                bmi_rounded = round(bmi, 1)
                category, advice = get_bmi_category_and_advice(bmi)
                return render_template('result.html', bmi=bmi_rounded, category=category, advice=advice, weight=weight_val, height=height_val)
        except ValueError:
            error = '請確認數值輸入為數字（例如：體重 70，身高 175 或 1.75）。'

        return render_template('index.html', error=error, weight=weight, height=height)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
