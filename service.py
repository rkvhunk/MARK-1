import os
from flask import request, redirect, jsonify, Blueprint, request, render_template
from flasgger import swag_from
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

db = SQLAlchemy()

SERVICE = Blueprint("service", __name__)

NER = None


@SERVICE.route("/check", methods=['GET'])
@swag_from("hello_world.yml")
def hello():
    return {'status': 'success'}

@SERVICE.route("/spacy", methods=['POST'])
@swag_from("spacy.yml")
def spacy():
    if request.method == 'POST':
        file_data = request.files.get("file")
        import spacy
        from spacy import displacy

        ORG = spacy.explain("ORG")
        GPE = spacy.explain("GPE")
        PRODUCT = spacy.explain("PRODUCT")
        LOC = spacy.explain("LOC")
        DATE = spacy.explain("DATE")
        ORDINAL = spacy.explain("ORDINAL")
        MONEY = spacy.explain("MONEY")
        print(f"ORG : {ORG}")
        print(f"GPE : {GPE}")
        print(f"PRODUCT: {PRODUCT}")
        print(f"LOC : {LOC}")
        print(f"DATE : {DATE}")
        print(f"ORDINAL : {ORDINAL}")
        print(f"MONEY : {MONEY}")

        
        NER = spacy.load("en_core_web_sm")
        
        text="The Indian Space Research Organisation or is the national space agency of India, headquartered in Bengaluru. It operates under Department of Space which is directly overseen by the Prime Minister of India while Chairman of ISRO acts as executive of DOS as well."
        
        data = NER(text)
        
        for entities in data.ents:
            print(entities.text, entities.label_)
        
        # displacy.render(data)
        displacy.render(data,style="ent",jupyter=True)
        return {'status': 'success'}

@SERVICE.route("/nltk", methods=['POST'])
@swag_from("nltk.yml")
def nltk():
    if request.method == 'POST':
        file_to_upload = request.files['file']
        
        import nltk
        from nltk.tokenize import word_tokenize
        from nltk.tag import pos_tag
        
        ex = 'European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices'
        sent = nltk.word_tokenize(ex)
        sent = nltk.pos_tag(ex)

        return {'status': 'success', 'result':sent}

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(80), unique=True, nullable=False)
    color = db.Column(db.String(120), nullable=False)