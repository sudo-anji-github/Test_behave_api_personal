from behave import *
import requests
from utils.common_methods import subscription_post
import sys, pdb;

@given(u'the user collects the base subscription details')
def step_impl(context):
    context.payload, context.url, context.headers = subscription_post(context)

@when(u'the user tries to create a new subscription')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payload, headers=context.headers)
    print(context.response.status_code)
    print(context.response.json())  # For checking the response content


@then(u'the new subscription should be created with a response status code of {response_status}')
def step_impl(context, response_status):
    #pdb.Pdb(stdout=sys.__stdout__).set_trace()
    assert context.response.status_code == int(response_status), "Subscription was not created successfully"

@then(u'the subscription name in the response should match the given payload')
def step_impl(context):
    #pdb.Pdb(stdout=sys.__stdout__).set_trace()
    assert context.response.json()['name'] == context.payload['name'], "Not matched...."