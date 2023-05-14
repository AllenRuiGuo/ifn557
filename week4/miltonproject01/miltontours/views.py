from flask import Blueprint, render_template, url_for, request, session, flash
from .models import City, Tour, Order
from datetime import datetime
from .forms import CheckoutForm


bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    #return render_template('index.html', cities = cities)
    return render_template('index.html')

@bp.route('/tours/<int:cityid>/')
def citytours(cityid):
    #return render_template('citytours.html', tours = tours)
    return render_template('citytours.html')


# STUBS for routes not implemented yet
# (get_url links in the templates will fail without these routes defined)

@bp.route('/order/', methods=['POST','GET'])
def order():
    #return render_template('order.html', order = order, totalprice = order.total_cost)
    return 'not implemented yet'


@bp.route('/deleteorder/')
def deleteorder():
    #return render_template('index.html')
    return 'not implemented yet'

@bp.route('/deleteorderitem/', methods=['POST'])
def deleteorderitem():
    #return render_template('index.html')
    return 'not implemented yet'


@bp.route('/checkout/', methods=['POST','GET'])
def checkout():
    #return render_template('checkout.html', form = form)
    return 'not implemented yet'