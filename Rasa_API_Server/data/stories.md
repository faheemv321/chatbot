<!-- START BASE STORIES -->

## AFFIRM
* affirm
  - utter_affirm

## DENY
* deny
  - utter_sorry

<!-- START GOODBYE -->
## GOODBYE 1
* goodbye
  - utter_goodbye

## GOODBYE 2
* goodbye
  - utter_affirm_goodbye
* goodbye
  - utter_goodbye
<!-- END GOODBYE -->

## GREET
* greet
  - utter_greet

## GST BASIC INFORMATION
* gst-basic-info
  - utter_gst_basic_info

<!-- START GST GOODS WITH GIVEN RATE -->
## GOODS WITH 5% GST RATE
* goods-with-given-rate{"rate":"5"}
  - utter_gst_5_goods

## GOODS WITH 12% GST RATE
* goods-with-given-rate{"rate":"12"}
  - utter_gst_12_goods

## GOODS WITH 18% GST RATE
* goods-with-given-rate{"rate":"18"}
  - utter_gst_18_goods

## GOODS WITH 28% GST RATE
* goods-with-given-rate{"rate":"28"}
  - utter_gst_28_goods
<!-- END GST GOODS WITH GIVEN RATE -->

<!-- START GST EXEMPT GOODS/SERVICE -->
## GST EXEMPT GOODS
* gst-exempt{"goods/services":"goods"}
  - utter_gst_exempt_goods

## GST EXEMPT SERVICES
* gst-exempt{"goods/services":"services"}
  - utter_gst_exempt_services
<!-- END GST EXEMPT GOODS/SERVICE -->



## BOT INTRODUCTION
* bot-intro
  - utter_bot_intro 

# MOOD GREAT
* mood-great
  - utter_happy
<!-- END BASE STORIES -->


<!-- START SHAUN STORIES -->

<!-- START GST COMPOSITION SCHEME -->
# GST COMPOSITION SCHEME INTRODUCTION
* gst-scheme-intro{"scheme":"composition"}
  - utter_gst_composition_scheme

## GST COMPOSITION SCHEME INELIGIBLE
* gst-scheme-ineligible-info{"scheme":"composition"}
  - utter_gst_composition_scheme_ineligible

## GST COMPOSITION SCHEME RULES
* gst-scheme-rules{"scheme":"composition"}
  - utter_gst_composition_scheme_rules

## GST COMPOSITION SCHEME DEADLINE
* gst-scheme-deadline{"scheme":"composition"}
  - utter_gst_composition_scheme_deadline

## GST COMPOSITION SCHEME RATES
* gst-scheme-rates{"scheme":"composition"}
  - utter_gst_composition_scheme_rates

## GST COMPOSITION SCHEME RETURN FILING INFORMATION
* gst-scheme-return-filing-info{"scheme":"composition"}
  - utter_gst_composition_scheme_return_info

## GST COMPOSITION SCHEME ADVANTAGES
* gst-scheme-advantages{"scheme":"composition"}
  - utter_gst_composition_scheme_advantages

## GST COMPOSITION SCHEME DISADVANTAGES
* gst-scheme-disadvantages
  - utter_gst_composition_scheme_disadvantages
<!-- END GST COMPOSITION SCHEME -->

<!-- START GST PENALTY -->
## GST LATE FILING PENALTY
* gst-late-filing-penalty
  - utter_gst_late_filing_penalty

## GST REGISTRATION CANCELLATION CIRCUMSTANCES
* gst-registration-cancellation-circumstances
  - utter_gst_cancellation_circumstances

## GST IMPRISONMENT CIRCUMSTANCES
* gst-imprisonment-circumstances
  - utter_imprisonment_circumstances
<!-- END GST PENALTY -->

<!-- START GST TYPES: CGST, SGST, IGST -->
## CGST FULL FORM
* gst-type-full-form{"gst-type":"cgst"}
  - utter_cgst_full_form

## CGST INTRODUCTION
* gst-type-intro{"gst-type":"cgst"}
  - utter_cgst_intro

## SGST FULL FORM
* gst-type-full-form{"gst-type":"sgst"}
  - utter_sgst_full_form

## SGST INTRODUCTION
* gst-type-intro{"gst-type":"sgst"}
  - utter_sgst_intro

## IGST FULL FORM
* gst-type-full-form{"gst-type":"igst"}
  - utter_igst_full_form

## IGST INTRODUCTION
* gst-type-intro{"gst-type":"igst"}
  - utter_igst_intro
<!-- END GST TYPES: CGST, SGST, IGST -->

<!-- END SHAUN STORIES -->

<!-- START FAHEEM STORIES -->

<!-- START GST REGISTRATION-->
## GST REGISTRATION CANCELLATION BY OFFICER

* gst-registration-cancellation-by-officer
    - utter_gst_cancellation_by_officer

## DOCUMENTS FOR GST REGISTRATION

* documents-for-gst-registration
    - utter_gst_registration_documents

## GST DOCUMENTS FORMAT

* gst-documents-format
    - utter_gst_registration_document_format

## MANDATORY CATEGORIES FOR GST REGISTRATION

* gst-mandatory-registration-category
    - utter_mandatory_gst_registration_category

## GST CANCELLATION ONLINE

* gst-registration-cancellation-online
    - utter_gst_registration_cancellation_online

## GST REGISTRATION ELIGIBILITY

* gst-registration-eligibility
    - utter_gst_registration_eligibility

## GST REGISTRATION PROCESS

* gst-registration-process
    - utter_gst_registration_procedure

## GST REGISTRATION STATUS 

* gst-registration-status-check
    - utter_gst_registration_status_check
<!-- END GST REGISTRATION-->

<!-- END FAHEEM STORIES -->


<!-- START SUBASH STORIES -->


<!-- START GST RATE OF PRODUCT -->

<!-- START 5% GST GOODS-->

## YARN
* gst-rate-of-product{"product":"yarn textile"}
    - utter_5

## NATURAL FIBRE
* gst-rate-of-product{"product":"natural fibre textile"}
    - utter_5

## COTTON TEXTILE
* gst-rate-of-product{"product":"cotton textile"}
    - utter_5

## LIFEBOAT
* gst-rate-of-product{"product":"lifeboat"}
    - utter_5

## STENTS
* gst-rate-of-product{"product":"stents"}
    - utter_5

## MEDICINES

* gst-rate-of-product{"product":"medicines"}
    - utter_5

## BROOM

* gst-rate-of-product{"product":"broom"}
    - utter_5

## SOLAR PANELS

* gst-rate-of-product{"product":"solar panels"}
    - utter_5

## INCENSE STICKS

* gst-rate-of-product{"product":"incense sticks"}
    - utter_5

## COAL
* gst-rate-of-product{"product":"coal"}
    - utter_5

## LPG
* gst-rate-of-product{"product":"LPG"}
    - utter_5

## KEROSENE
* gst-rate-of-product{"product":"kerosene"}
    - utter_5

## JUICES
* gst-rate-of-product{"product":"juices"}
    - utter_5

## TEA
* gst-rate-of-product{"product":"tea"}
    - utter_5  

## COFFEE
* gst-rate-of-product{"product":"coffee"}
    - utter_5    

## TAPIOCA
* gst-rate-of-product{"product":"tapioca"}
    - utter_5    

## SWEETS
* gst-rate-of-product{"product":"sweets"}
    - utter_5

## RUSK
* gst-rate-of-product{"product":"rusk"}
    - utter_5

## PIZZA
* gst-rate-of-product{"product":"pizza bread"}
    - utter_5

## EDIBLE OIL
* gst-rate-of-product{"product":"edible oil"}
    - utter_5

## SPICES
* gst-rate-of-product{"product":"spices"}
    - utter_5

## SUGAR
* gst-rate-of-product{"product":"sugar"}
    - utter_5

## FROZEN VEGETABLES
* gst-rate-of-product{"product":"frozen vegetables"}
    - utter_5

## CREAM
* gst-rate-of-product{"product":"cream"}
    - utter_5

## CONDENSED MILK
* gst-rate-of-product{"product":"condensed milk"}
    - utter_5       

## PACKAGED PANEER
* gst-rate-of-product{"product":"packaged paneer"}
    - utter_5

## SKIMMED MILK POWDER
* gst-rate-of-product{"product":"skimmed milk powder"}
    - utter_5
<!-- END 5% GST GOODS -->

<!-- START 12% GST GOODS -->
## MOBILE PHONES
* gst-rate-of-product{"product":" mobile phones"}
    - utter_12

## AYURVEDIC MEDICINE
* gst-rate-of-product{"product":"ayurvedic medicine"}
    - utter_12

## UMBRELLA
* gst-rate-of-product{"product":"umbrella"}
    - utter_12

## SEWING MACHINE
* gst-rate-of-product{"product":"sewing machine"}
    - utter_12

## NOTEBOOK
* gst-rate-of-product{"product":"notebooks"}
    - utter_12

## EXERCISE NOTEBOOKS
* gst-rate-of-product{"product":"exercise notebooks"}
    - utter_12

## TOOTH POWDER
* gst-rate-of-product{"product":"tooth powder"}
    - utter_12

## COCONUT WATER
* gst-rate-of-product{"product":"packed coconut water"}
    - utter_12

## FRUIT JUICES 
* gst-rate-of-product{"product":"fruit juices"}
    - utter_12

## SAUCES
* gst-rate-of-product{"product":"sauces"}
    - utter_12

## JAM
* gst-rate-of-product{"product":"jam"}
    - utter_12

## SAUSAGES
* gst-rate-of-product{"product":"sausages"}
    - utter_12

## PACKAGED CHICKED
* gst-rate-of-product{"product":"packaged chicken"}
    - utter_12

## SNACKS
* gst-rate-of-product{"product":"snacks"}
    - utter_12

## PACKAGED DRY FRUITS
* gst-rate-of-product{"product":"packaged dry fruits"}
    - utter_12

## CHEESE
* gst-rate-of-product{"product":"cheese"}
    - utter_12

## GHEE
* gst-rate-of-product{"product":"ghee"}
    - utter_12

## BUTTER
* gst-rate-of-product{"product":"butter"}
    - utter_12
<!-- END 12% GST -->

<!-- START 18% GST -->
## MAN MADE FIBRE
* gst-rate-of-product{"product":"man-made-fibre textile"}
    - utter_18

## BISCUITS
* gst-rate-of-product{"product":"biscuits"}
    - utter_18

## STEEL
* gst-rate-of-product{"product":"steel"}
    - utter_18

## IRON
* gst-rate-of-product{"product":"iron"}
    - utter_18

## IRON AND STEEL PRODUCTS
* gst-rate-of-product{"product":"iron and steel products"}
    - utter_18

## MONITORS
* gst-rate-of-product{"product":"monitors"}
    - utter_18

## PRINTED CIRCUIT BOARDS
* gst-rate-of-product{"product":"printed circuit boards"}
    - utter_18

## FOUNTAIN PENS
* gst-rate-of-product{"product":"fountain pens"}
    - utter_18

## ENVELOPES
* gst-rate-of-product{"product":"envelopes"}
    - utter_18

## TOOTHPASTE
* gst-rate-of-product{"product":"toothpaste"}
    - utter_18

## SOAP
* gst-rate-of-product{"product":"soap"}
    - utter_18

## HAIR OIL
* gst-rate-of-product{"product":"hair oil"}
    - utter_18

## TOILET PAPER
* gst-rate-of-product{"product":"toilet paper"}
    - utter_18

## TISSUES
* gst-rate-of-product{"product":"tissues"}
    - utter_18

## BRANDED GARMENTS
* gst-rate-of-product{"product":"branded garments"}
    - utter_18

## MINERAL WATER
* gst-rate-of-product{"product":"mineral water"}
    - utter_18

## PROCESSED FOODS
* gst-rate-of-product{"product":"processed foods"}
    - utter_18

## INSTANT FOOD MIXES
* gst-rate-of-product{"product":"instant food mixes"}
    - utter_18

## SOUPS
* gst-rate-of-product{"product":"soups"}
    - utter_18

## CAKES
* gst-rate-of-product{"product":"cakes"}
    - utter_18

## PASTRIES
* gst-rate-of-product{"product":"pastries"}
    - utter_18

## CORN FLAKES
* gst-rate-of-product{"product":"corn flakes"}
    - utter_18

## PASTA
* gst-rate-of-product{"product":"pasta"}
    - utter_18

## FLAVOURED SUGAR
* gst-rate-of-product{"product":"flavoured sugar"}
    - utter_18

## PRESERVED VEGETABLES
* gst-rate-of-product{"product":"preserved vegetables"}
    - utter_18

## ICE CREAM
* gst-rate-of-product{"product":"ice creams"}
    - utter_18
<!-- END 18% GST -->

<!-- START 28% GST -->
## BIDIS
* gst-rate-of-product{"product":"bidis"}
    - utter_28

## PAAN MASALA
* gst-rate-of-product{"product":"paan masala"}
    - utter_28

## FIREWORKS
* gst-rate-of-product{"product":"fireworks"}
    - utter_28

## ATM MACHINE
* gst-rate-of-product{"product":"ATM machine"}
    - utter_28

## VENDING MACHINE
* gst-rate-of-product{"product":"vending machine"}
    - utter_28

## WEIGHING MACHINE
* gst-rate-of-product{"product":"weighing machine"}
    - utter_28

## CEMENT
* gst-rate-of-product{"product":"cement"}
    - utter_28

## CERAMIC TILES
* gst-rate-of-product{"product":"ceramic tiles"}
    - utter_28

## WALLPAPERS
* gst-rate-of-product{"product":"wallpapers"}
    - utter_28

## PAINT
* gst-rate-of-product{"product":"paint"}
    - utter_28

## AUTOMOBILE
* gst-rate-of-product{"product":"automobiles and motor vehicles"}
    - utter_28

## CAMERA
* gst-rate-of-product{"product":"camera"}
    - utter_28

## SPEAKERS
* gst-rate-of-product{"product":"speakers"}
    - utter_28

## HOME APPLIANCES
* gst-rate-of-product{"product":"home appliances"}
    - utter_28

## WATER HEATERS
* gst-rate-of-product{"product":"water heaters"}
    - utter_28

## DISH WASHERS
* gst-rate-of-product{"product":"dish washers"}
    - utter_28

## WASHING MACHINE
* gst-rate-of-product{"product":"washing machine"}
    - utter_28

## HAIR CLIPPERS
* gst-rate-of-product{"product":"hair clippers"}
    - utter_28

## SHAVERS
* gst-rate-of-product{"product":"shavers"}
    - utter_28

## VACUMM CLEANER
* gst-rate-of-product{"product":"vacuum cleaner"}
    - utter_28

## DETERGENTS
* gst-rate-of-product{"product":"detergents"}
    - utter_28

## FACE CREAMS
* gst-rate-of-product{"product":"face creams"}
    - utter_28

## PERFUME
* gst-rate-of-product{"product":"perfume"}
    - utter_28

## SUNSCREEN
* gst-rate-of-product{"product":"sunscreen"}
    - utter_28

## DYE
* gst-rate-of-product{"product":"dye"}
    - utter_28

## HAIR SHAMPOO
* gst-rate-of-product{"product":"hair shampoo"}
    - utter_28

## AFTER SHAVE
* gst-rate-of-product{"product":"after shave"}
    - utter_28

## SHAVING CREAM
* gst-rate-of-product{"product":"shaving cream"}
    - utter_28

## DEODORANTS
* gst-rate-of-product{"product":"deodorants"}
    - utter_28

## AERATED WATER
* gst-rate-of-product{"product":"aerated water"}
    - utter_28

## CUSTARD POWDER
* gst-rate-of-product{"product":"custard powder"}
    - utter_28

## CHEWING GUM
* gst-rate-of-product{"product":"chewing gum"}
    - utter_28

## CHOCOLATES
* gst-rate-of-product{"product":"chocolates"}
    - utter_28
<!-- END 28% GST GOODS -->

<!-- START GST MISC -->
## SEMIPRECIOUS STONES
* gst-rate-of-product{"product":"semi-precious stones"}
    - utter_0.25

## JEWELLERY
* gst-rate-of-product{"product":"jewellery"}
    - utter_3

## GEMS
* gst-rate-of-product{"product":"gems"}
    - utter_3

## GOLD
* gst-rate-of-product{"product":"gold"}
    - utter_3



## ESSENTIAL GOODS
* gst-rate-of-product{"product":"essential goods"}
    - utter_essential

## STANDARD GOODS
* gst-rate-of-product{"product":"standard goods"}
    - utter_standard

## LUXURY GOODS
* gst-rate-of-product{"product":"luxury goods"}
    - utter_luxury
<!-- START GST MISC -->

<!-- START GST EXEMPT -->
## MILK
* gst-rate-of-product{"product":"milk"}
    - utter_exempt

## CURD
* gst-rate-of-product{"product":"curd"}
    - utter_exempt

## BUTTER MILK
* gst-rate-of-product{"product":"butter milk"}
    - utter_exempt

## LASSI
* gst-rate-of-product{"product":"lassi"}
    - utter_exempt

## POULTRY PRODUCTS
* gst-rate-of-product{"product":"poultry products"}
    - utter_exempt

## CONTRACEPTIVES
* gst-rate-of-product{"product":"contraceptives"}
    - utter_exempt

## SILK TEXTILE
* gst-rate-of-product{"product":"silk textile"}
    - utter_exempt

## JUTE TEXTILE
* gst-rate-of-product{"product":"jute textile"}
    - utter_exempt

## HANDLOOM PRODUCTS
* gst-rate-of-product{"product":"handloom products"}
    - utter_exempt

## NEWSPAPER
* gst-rate-of-product{"product":"newspaper"}
    - utter_exempt

## PRINTED BOOKS
* gst-rate-of-product{"product":"printed books"}
    - utter_exempt

## JUDICIAL PAPERS
* gst-rate-of-product{"product":"judiacial papers"}
    - utter_exempt

## STAMP
* gst-rate-of-product{"product":"stamp"}
    - utter_exempt

## BANGLES
* gst-rate-of-product{"product":"bangles"}
    - utter_exempt

## BINDI
* gst-rate-of-product{"product":"bindi"}
    - utter_exempt

## SALT
* gst-rate-of-product{"product":"salt"}
    - utter_exempt

## VEGETABLE OIL
* gst-rate-of-product{"product":"vegetable oil"}
    - utter_exempt

## BREAD
* gst-rate-of-product{"product":"bread"}
    - utter_exempt

## GRAM FLOUR
* gst-rate-of-product{"product":"gram flour"}
    - utter_exempt

## BASMATI RICE
* gst-rate-of-product{"product":"basmati rice"}
    - utter_exempt

## PULSES
* gst-rate-of-product{"product":"pulses"}
    - utter_exempt

## FLOUR
* gst-rate-of-product{"product":"flour"}
    - utter_exempt

## HONEY
* gst-rate-of-product{"product":"honey"}
    - utter_exempt

## VEGETABLES
* gst-rate-of-product{"product":"vegetables"}
    - utter_exempt

## FRUITS
* gst-rate-of-product{"product":"fruits"}
    - utter_exempt

## CHICKEN
* gst-rate-of-product{"product":"chicken"}
    - utter_exempt

## FISH
* gst-rate-of-product{"product":"fish"}
    - utter_exempt

## FRESH MEAT
* gst-rate-of-product{"product":"fresh meat"}
    - utter_exempt

## EGGS
* gst-rate-of-product{"product":"eggs"}
    - utter_exempt
<!-- END GST EXEMPT -->

<!-- END GST RATE OF PRODUCT -->

<!-- START GST RATE OF SERVICES -->
## CAB AGGREGATORS
* gst-rate-of-services{"service":"cab aggregators"}
    - utter_5

## UBER
* gst-rate-of-services{"service":"cab"}
    - utter_5

## OLA
* gst-rate-of-services{"service":"ola"}
    - utter_5

## ECO AIR TICKET
* gst-rate-of-services{"service":"economy class air ticket"}
    - utter_5

## RAILWAY
* gst-rate-of-services{"service":"railway"}
    - utter_5

## NON AC HOTELS
* gst-rate-of-services{"service":"non-ac hotels"}
    - utter_12

## BUSINESS AIR TICKETS
* gst-rate-of-services{"service":"business class air ticket"}
    - utter_12

## CINEMA TICKETS
* gst-rate-of-services{"service":"cinema tickets"}
    - utter_18

## TELECOM
* gst-rate-of-services{"service":"telecom services"}
    - utter_18

## FINANCIAL
* gst-rate-of-services{"service":"financial services"}
    - utter_18

## IT
* gst-rate-of-services{"service":"IT services"}
    - utter_18

## WORK CONTRACT
* gst-rate-of-services{"service":"work contract"}
    - utter_18

## AC HOTELS
* gst-rate-of-services{"service":"AC hotels"}
    - utter_18

<!-- END GST RATE OF SERVICES -->
<!-- END SUBASH STORIES -->

<!-- START SARIN STORIES -->
<!-- START GST E-WAY BILL -->
## E-WAY BILL INTRODUCTION
* gst-E-way-bill-intro
    - utter_gst_e_way_bill_intro

## E-WAY BILL WHEN APPLICABLE
* gst-E-way-bill-when-applicable
    - utter_when_applicable

## E-WAY BILL REFERENCE NUMBER
* reference-number-in-E-way-bill
    - utter_gst_reference_number_E_way_bill
<!-- END GST E-WAY BILL -->

<!-- START GST PAYMENT-->
## GST-PAYMENT CALCULATION

* gst-payment-calculation
    - utter_gst_payment_calculate

## GST-BUSINESS-PAYMENT-METHOD
* gst-business-payment-method
    - utter_gst_business_payment_method


## GST-REFUND
* gst-refund-claim
    - utter_gst_refund_claim

## IMPORT/EXPORT
* gst-import-export-info{"import/export":"import"}
    - utter_gst_import
<!-- END GST PAYMENT-->

<!-- START GST BENEFITS -->
## GST-BENEFIT IN MARKET

* gst-benefits-info{"benefit-category":"market"}
    - utter_gst_benefits_market

## GST-BENEFIT-IN DEVELOPED STATES

* gst-benefits-info{"benefit-category":"under developed states"}
    - utter_under_developed_states

## GST-BENEFITS-TAXPAYERS

* gst-benefits-info{"benefit-category":"small tax payers"}
    - utter_gst_benefits_small_taxpayers

## GST-BENEFIT-COUNTRY

* gst-benefits-info{"benefit-category":"Country"}
    - utter_gst_benefits_country
<!-- END GST BENEFITS -->

<!-- END SARIN STORIES -->