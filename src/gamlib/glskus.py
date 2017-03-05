# -*- coding: utf-8 -*-

# Copyright (C) 2016 Ross Scroggs All Rights Reserved.
#
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Google SKUs

"""

import re

# Products/SKUs
_SKUS = {
  'Google-Apps-For-Business': {
    'product': 'Google-Apps', 'aliases': ['gafb', 'gafw', 'basic', 'gsuitebasic'], 'displayName': 'G Suite Basic'},
  'Google-Apps-For-Government': {
    'product': 'Google-Apps', 'aliases': ['gafg', 'gsuitegovernment', 'gsuitegov'], 'displayName': 'G Suite Government'},
  'Google-Apps-For-Postini': {
    'product': 'Google-Apps', 'aliases': ['gams', 'postini', 'gsuitegams', 'gsuitepostini', 'gsuitemessagesecurity'], 'displayName': 'G Suite Message Security'},
  'Google-Apps-Lite': {
    'product': 'Google-Apps', 'aliases': ['gal', 'lite', 'gsuitelite'], 'displayName': 'G Suite Lite'},
  'Google-Apps-Unlimited': {
    'product': 'Google-Apps', 'aliases': ['gau', 'unlimited', 'gsuitebusiness'], 'displayName': 'G Suite Business'},
  '1010020020': {
    'product': 'Google-Apps', 'aliases': ['gae', 'enterprise', 'gsuiteenterprise'], 'displayName': 'G Suite Enterprise'},
  'Google-Drive-storage-20GB': {
    'product': 'Google-Drive-storage', 'aliases': ['drive20gb', '20gb', 'googledrivestorage20gb'], 'displayName': 'Google Drive Storage 20GB'},
  'Google-Drive-storage-50GB': {
    'product': 'Google-Drive-storage', 'aliases': ['drive50gb', '50gb', 'googledrivestorage50gb'], 'displayName': 'Google Drive Storage 50GB'},
  'Google-Drive-storage-200GB': {
    'product': 'Google-Drive-storage', 'aliases': ['drive200gb', '200gb', 'googledrivestorage200gb'], 'displayName': 'Google Drive Storage 200GB'},
  'Google-Drive-storage-400GB': {
    'product': 'Google-Drive-storage', 'aliases': ['drive400gb', '400gb', 'googledrivestorage400gb'], 'displayName': 'Google Drive Storage 400GB'},
  'Google-Drive-storage-1TB': {
    'product': 'Google-Drive-storage', 'aliases': ['drive1tb', '1tb', 'googledrivestorage1tb'], 'displayName': 'Google Drive Storage 1TB'},
  'Google-Drive-storage-2TB': {
    'product': 'Google-Drive-storage', 'aliases': ['drive2tb', '2tb', 'googledrivestorage2tb'], 'displayName': 'Google Drive Storage 2TB'},
  'Google-Drive-storage-4TB': {
    'product': 'Google-Drive-storage', 'aliases': ['drive4tb', '4tb', 'googledrivestorage4tb'], 'displayName': 'Google Drive Storage 4TB'},
  'Google-Drive-storage-8TB': {
    'product': 'Google-Drive-storage', 'aliases': ['drive8tb', '8tb', 'googledrivestorage8tb'], 'displayName': 'Google Drive Storage 8TB'},
  'Google-Drive-storage-16TB': {
    'product': 'Google-Drive-storage', 'aliases': ['drive16tb', '16tb', 'googledrivestorage16tb'], 'displayName': 'Google Drive Storage 16TB'},
  'Google-Vault': {
    'product': 'Google-Vault', 'aliases': ['vault', 'googlevault'], 'displayName': 'Google Vault'},
  'Google-Vault-Former-Employee': {
    'product': 'Google-Vault', 'aliases': ['vfe', 'googlevaultformeremployee'], 'displayName': 'Google Vault Former Employee'},
  'Google-Coordinate': {
    'product': 'Google-Coordinate', 'aliases': ['coordinate', 'googlecoordinate'], 'displayName': 'Google Coordinate'},
  'Google-Chrome-Device-Management': {
    'product': 'Google-Chrome-Device-Management', 'aliases': ['chrome', 'cdm', 'googlechromedevicemanagement'], 'displayName': 'Google Chrome Device Management'}
  }

def getProductAndSKU(sku):
  l_sku = sku.lower().replace('-', '').replace(' ', '')
  for a_sku, sku_values in list(_SKUS.items()):
    if l_sku == a_sku.lower().replace('-', '') or l_sku in sku_values['aliases'] or l_sku == sku_values['displayName'].lower().replace(' ', ''):
      return (sku_values['product'], a_sku)
  try:
    product = re.search('^([A-Z,a-z]*-[A-Z,a-z]*)', sku).group(1)
  except AttributeError:
    product = sku
  return (product, sku)

def skuIdToDisplayName(skuId):
  return _SKUS[skuId]['displayName'] if skuId in _SKUS else skuId

def formatSKUIdDisplayName(skuId):
  skuIdDisplay = skuIdToDisplayName(skuId)
  if skuId == skuIdDisplay:
    return skuId
  return '{0} ({1})'.format(skuId, skuIdDisplay)

def normalizeProductId(product):
  l_product = product.lower().replace('-', '').replace(' ', '')
  for a_sku, sku_values in list(_SKUS.items()):
    if ((l_product == sku_values['product'].lower().replace('-', ''))
        or (l_product == a_sku.lower().replace('-', ''))
        or (l_product in sku_values['aliases'])
        or (l_product == sku_values['displayName'].lower().replace(' ', ''))):
      return sku_values['product']
  return product

def getSortedProductList():
  products = []
  for sku in list(_SKUS.values()):
    if sku['product'] not in products:
      products.append(sku['product'])
  products.sort()
  return products

def getSortedSKUList():
  return sorted(_SKUS.keys())

def convertProductListToSKUList(productList):
  skuList = []
  for productId in productList:
    skuList += [skuId for skuId in _SKUS if _SKUS[skuId]['product'] == productId]
  return skuList