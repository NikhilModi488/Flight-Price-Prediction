from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle
import pandas as pd
import bz2

app = Flask(__name__,template_folder='templates')
model = pickle.load(bz2.BZ2File("flight_prices.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        dep_date=request.form['dep_time']
        dep_f_date=pd.to_datetime(dep_date).date()
        dep_day= int(pd.to_datetime(dep_date).day)
        dep_month = int(pd.to_datetime(dep_date).month)

        dep_time=pd.to_datetime(dep_date).time()
        dep_hour = int(pd.to_datetime(dep_date).hour)
        dep_min = int(pd.to_datetime(dep_date).minute)

        arr_date=request.form['arr_time']
        arr_f_date=pd.to_datetime(arr_date).date()
        arr_f_time=pd.to_datetime(arr_date).time()
        arrival_hour = int(pd.to_datetime(arr_date).hour)
        arrival_min = int(pd.to_datetime(arr_date).minute)

        duration_hour=arrival_hour-dep_hour
        duration_min=arrival_min-dep_min

        stops=request.form['stopage']

        source=request.form['source']
        if source =='Delhi':
            Delhi=1
            Kolkata = 0
            Chennai = 0
            Mumbai = 0
        elif source=='Kolkata':
            Delhi = 0
            Kolkata = 1
            Chennai = 0
            Mumbai = 0
        elif source=='Chennai':
            Delhi = 0
            Kolkata = 0
            Chennai = 1
            Mumbai = 0
        elif source=='Mumbai':
            Delhi = 0
            Kolkata = 0
            Chennai = 0
            Mumbai = 1
        else:
            Delhi = 0
            Kolkata = 0
            Chennai = 0
            Mumbai = 0


        destination=request.form['destination']
        if destination=='Cochin':
            Cochin = 1
            delhi = 0
            N_delhi = 0
            hyderabad = 0
            kolkata = 0
        elif destination== 'Delhi':
            Cochin = 0
            delhi = 1
            N_delhi = 0
            hyderabad = 0
            kolkata = 0
        elif destination=='New Delhi':
            Cochin = 0
            delhi = 0
            N_delhi = 1
            hyderabad = 0
            kolkata = 0
        elif destination=='Hyderabad':
            Cochin = 0
            delhi = 0
            N_delhi = 0
            hyderabad = 1
            kolkata = 0
        elif destination=='Kolkata':
            Cochin = 0
            delhi = 0
            N_delhi = 0
            hyderabad = 0
            kolkata = 1
        else:
            Cochin = 0
            delhi = 0
            N_delhi = 0
            hyderabad = 0
            kolkata = 0


        airlines = request.form['airline']
        if airlines == 'IndiGo':
            indigo = 1
            air_india=0
            jet_airways=0
            trujet=0
            spicejet=0
            vistara=0
            goair=0
            multiple_carriers=0
            vistara_premium=0
            multiple_carrier_premium=0
            jet_airways_business=0
        elif airlines == 'Air India':
            indigo = 0
            air_india = 1
            jet_airways = 0
            trujet = 0
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers = 0
            vistara_premium = 0
            multiple_carrier_premium = 0
            jet_airways_business = 0
        elif airlines == 'Jet Airways':
            indigo = 0
            air_india = 0
            jet_airways = 1
            trujet = 0
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers = 0
            vistara_premium = 0
            multiple_carrier_premium = 0
            jet_airways_business = 0
        elif airlines == 'Trujet':
            indigo = 0
            air_india = 0
            jet_airways = 0
            trujet = 1
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers = 0
            vistara_premium = 0
            multiple_carrier_premium = 0
            jet_airways_business = 0
        elif airlines == 'SpiceJet':
            indigo = 0
            air_india = 0
            jet_airways = 0
            trujet = 0
            spicejet = 1
            vistara = 0
            goair = 0
            multiple_carriers = 0
            vistara_premium = 0
            multiple_carrier_premium = 0
            jet_airways_business = 0
        elif airlines == 'Vistara':
            indigo = 0
            air_india = 0
            jet_airways = 0
            trujet = 0
            spicejet = 0
            vistara = 1
            goair = 0
            multiple_carriers = 0
            vistara_premium = 0
            multiple_carrier_premium = 0
            jet_airways_business = 0
        elif airlines == 'GoAir':
            indigo = 0
            air_india = 0
            jet_airways = 0
            trujet = 0
            spicejet = 0
            vistara = 0
            goair = 1
            multiple_carriers = 0
            vistara_premium = 0
            multiple_carrier_premium = 0
            jet_airways_business = 0
        elif airlines == 'Multiple carriers':
            indigo = 0
            air_india = 0
            jet_airways = 0
            trujet = 0
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers = 1
            vistara_premium = 0
            multiple_carrier_premium = 0
            jet_airways_business = 0
        elif airlines == 'Vistara Premium economy':
            indigo = 0
            air_india = 0
            jet_airways = 0
            trujet = 0
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers = 0
            vistara_premium = 1
            multiple_carrier_premium = 0
            jet_airways_business = 0
        elif airlines == 'Multiple carriers Premium economy':
            indigo = 0
            air_india = 0
            jet_airways = 0
            trujet = 0
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers = 0
            vistara_premium = 0
            multiple_carrier_premium = 1
            jet_airways_business = 0
        elif airlines == 'Jet Airways Business':
            indigo = 0
            air_india = 0
            jet_airways = 0
            trujet = 0
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers = 0
            vistara_premium = 0
            multiple_carrier_premium = 0
            jet_airways_business = 1
        else:
            indigo = 0
            air_india = 0
            jet_airways = 0
            trujet = 0
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers = 0
            vistara_premium = 0
            multiple_carrier_premium = 0
            jet_airways_business = 0
        # 32 columns


        prediction=model.predict([[
            dep_day,
            dep_month,
            dep_hour,
            dep_min,
            arrival_hour,
            arrival_min,
            duration_hour,
            duration_min,
            stops,
            indigo,
            air_india,
            jet_airways,
            trujet,
            spicejet,
            vistara,
            goair,
            multiple_carriers,
            vistara_premium,
            multiple_carrier_premium,
            jet_airways_business,
            Delhi,
            Kolkata,
            Chennai,
            Mumbai,
            Cochin,
            delhi,
            N_delhi,
            kolkata,
            hyderabad
        ]])
        output=round(prediction[0])

        return render_template('home.html',prediction=output, dep_day=dep_f_date, dep_time=dep_time, arr_date=arr_f_date, arr_time=arr_f_time, source=source, destination=destination,
                               stops=stops,airlines=airlines)


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
