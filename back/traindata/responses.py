from ..common_imports import *
from flask.views import MethodView
from flask_smorest import Blueprint
from ..utils import create_model

blp = Blueprint("responses", __name__, description="Operations on responses")


class ResponseModel(db.Model):
    __tablename__ = "responses"

    id = db.Column(db.Integer, primary_key=True)
    response = db.Column(db.String)
    intent_id = db.Column("intentid", db.Integer, db.ForeignKey("intents.id"), nullable=False)
    language = db.Column(db.String(2), nullable=False)
    intent = db.relationship("IntentModel", back_populates="responses")


class ResponseSchema(Schema):
    id = fields.Str(dump_only=True)
    response = fields.Str(required=True)
    intent_id = fields.Int(data_key='intentid', attribute='intent_id', required=True)
    language = fields.Str(required=True)


@blp.route("/responses")
class Response(MethodView):
    @blp.arguments(ResponseSchema)
    @blp.response(200, ResponseSchema)
    def post(self, response_data):
        response = create_model(ResponseModel, response_data)
        return response


greetings_responses = [
"Hartelijk welkom!",
"Welkom!",
"Hallo daar!",
"Hoi, wat kan ik doen om uw bezoek nog aangenamer te maken?",
"Hallo, bent u klaar om verrast te worden door onze culinaire creaties?",
"Hoi, bent u op zoek naar een smaakvolle ervaring?",
"Goedenavond, wat mag ik voor u betekenen vandaag?",
"Hallo, wilt u genieten van een heerlijke maaltijd?",
"Goeiedag, bent u klaar om te genieten van onze gastvrijheid?",
"Goedemorgen, op zoek naar een energierijke start van de dag?",
"Welkom terug, heeft u al zin in uw favoriete gerecht?",
"Hallo, hoe kan ik uw culinaire wensen vervullen?",
"Goedemiddag, heeft u al een voorkeur voor een gerecht?",
"Hoi, wilt u iets nieuws proberen of een klassieker bestellen?",
"Hallo, hoe kan ik uw bezoek speciaal maken?",
"Goeiemorgen, wat kan ik u aanbevelen vandaag?",
"Hallo, heeft u al trek gekregen?",
"Goedenavond, welkom bij ons gezellige café!",
"Hoi, op zoek naar iets om uw honger te stillen?",
"Hallo daar, hoe kan ik uw dag nog beter maken?",
"Hallo, wilt u zich laten verrassen door ons menu?",
"Goedendag, wat mag het vandaag voor u zijn?",
"Hallo, bent u klaar voor een culinaire ervaring?",
"Hallo, wat brengt u vandaag naar ons café?",
"Hoi, heeft u zin in een heerlijke maaltijd?",
"Goedemiddag, op zoek naar iets specifieks?",
"Welkom terug, we hebben u gemist!",
"Hallo, op zoek naar iets hartigs of iets zoets?",
"Goeiedag, klaar om uw smaakpapillen te verwennen?",
"Hallo, hoe kan ik u van dienst zijn?",
"Hallo, fijn dat u er bent!",
"Hoi, wat kan ik voor u doen?",
"Welkom terug!",
"Hallo, hoe gaat het met u vandaag?",
"Goedemorgen, klaar om te bestellen?",
"Goeiemorgen, op zoek naar iets lekkers?",
"Goedenavond, bent u klaar om te genieten van ons menu?",
"Hi, wat kan ik voor u betekenen?",

]
bestellen_responses = [
"Helaas hebben we geen speciale verzoekgerechten die niet op het menu staan.",
"Sorry, maar het gewenste gerecht staat niet op het menu en kan niet worden besteld.",
"Excuses, maar we kunnen geen gerechten bereiden die niet op het menu staan.",
"Sorry, maar we hebben geen mogelijkheid om gerechten te maken die niet op het menu staan.",
"Helaas bieden we geen maatwerkbestellingen aan die niet op het menu staan.",
"Sorry, maar het gewenste gerecht is niet beschikbaar en staat ook niet op het menu.",
"Excuses, maar we hebben geen mogelijkheid om gerechten te serveren die niet op het menu staan.",
"Helaas hebben we geen speciale verzoekgerechten die niet op het menu staan.",
"Sorry, maar het gewenste gerecht is niet beschikbaar en kan niet worden bereid.",
"Excuses, maar het gewenste gerecht is niet beschikbaar en staat niet op het menu.",
"Helaas kunnen we geen gerechten serveren die niet op het menu staan.",
"Sorry, maar het gewenste gerecht staat niet op het menu en kan niet worden geserveerd."
"Helaas is de kipsalade momenteel niet beschikbaar. Kan ik u iets anders aanbevelen?",
"Excuses, maar de appeltaart is uitverkocht. Mag ik u een ander dessert voorstellen?",
"Sorry, maar de nacho's zijn op. Is er nog iets anders waar ik u mee kan helpen?",
"We hebben momenteel geen vegetarische pizza. Kan ik u een ander vegetarisch gerecht aanbevelen?",
"Helaas hebben we geen club sandwiches meer. Kan ik u iets anders aanbieden van onze broodjeskaart?",
"Excuses, maar de cheesecake is uitverkocht. Mag ik u een ander taartje aanraden?",
"Sorry, maar we hebben geen sushi op het menu staan. Kan ik u iets anders uit onze Japanse gerechten aanbieden?",
"We hebben geen spaghetti meer. Kan ik u een ander pastagerecht aanbevelen?",
"Helaas hebben we momenteel geen vegetarische burger. Mag ik u een ander vegetarisch gerecht voorstellen?",
"Sorry, maar de tomatensoep is op. Kan ik u een andere soep aanbieden?",
"Excuses, maar de chocoladetaart is uitverkocht. Mag ik u een ander dessert aanbieden?",
"We hebben geen loempia's op het menu staan. Kan ik u een ander Aziatisch gerecht aanbevelen?",
"Helaas is de biefstuk momenteel niet beschikbaar. Kan ik u een ander vleesgerecht aanbieden?",
"Sorry, maar de garnalencocktail is op. Kan ik u een ander voorgerecht aanraden?",
"We hebben de kipsalade op voorraad.",
"Goed nieuws, we hebben appeltaart beschikbaar.",
"Ja, we hebben nacho's op het menu.",
"Onze vegetarische pizza is beschikbaar.",
"We hebben zalmfilet op het menu.",
"Goed om te horen dat u een club sandwich wilt bestellen.",
"Cheesecake is beschikbaar.",
"U kunt sushi bestellen.",
"We hebben spaghetti op het menu staan.",
"Onze vegetarische burger is beschikbaar.",
"Tomatensoep is beschikbaar.",
"Chocoladetaart is beschikbaar.",
"Helaas hebben we geen loempia's op het menu staan. Kunt u een ander gerecht kiezen?",
"Helaas hebben we momenteel geen biefstuk beschikbaar. Kan ik u helpen met een ander gerecht?",
"De garnalencocktail is beschikbaar.",
"U kunt de Caesar-salade bestellen.",
"Carrot cake is beschikbaar.",
"We hebben sushi op het menu.",
"Goed nieuws, zoete aardappelfriet is beschikbaar.",
"Ja, we hebben pad thai op het menu.",
"De veggie wrap is beschikbaar.",
"We hebben groentesoep op het menu staan.",
"U kunt red velvet cake bestellen.",
"Helaas hebben we geen dim sum op het menu staan. Kunt u een ander gerecht kiezen?",
"Helaas hebben we geen schnitzel op het menu. Kan ik u helpen met een ander gerecht?"
]
menu_responses = [
"Natuurlijk, hier is de menukaart.",
"Hier is een exemplaar van onze menukaart.",
"Ja, we hebben een menu beschikbaar. Hier is het.",
"Absoluut, laat me je de menu-opties laten zien.",
"Natuurlijk, ik zal je vertellen wat er op het menu staat.",
"Hier is een lijst met de gerechten die we aanbieden.",
"Ja, hier is de lijst met onze gerechten.",
"Zeker, hier zijn de menu-opties en prijzen.",
"Alsjeblieft, hier is de menukaart. Neem de tijd om je keuze te maken.",
"De menukaart bevindt zich aan de voorkant van het restaurant.",
"Natuurlijk, neem een kijkje op het menu.",
"Hier is de menukaart. Laat me weten als je vragen hebt.",
"We hebben een menu beschikbaar. Hier is het voor je.",
"Je kunt de menukaart even lenen om je keuze te maken.",
"Laten we eens kijken naar wat er op het menu staat. Hier zijn de gerechten.",
"We hebben ook speciale aanbiedingen. Hier is een overzicht van de menu-opties en aanbiedingen.",
"Natuurlijk, hier is de volledige menukaart, inclusief drankjes.",
"Zeker, hier zijn de menu-opties en prijzen om je te helpen bij het plaatsen van je bestelling.",
"Ja, we hebben een aparte menukaart met vegetarische en veganistische opties.",
"Neem gerust de menukaart en blader erdoorheen om je keuze te maken.",
"Hier is de lijst met gerechten die we aanbieden.",
"Zeker, hier zijn alle beschikbare gerechten die we op dit moment serveren.",
"Onze menukaart is beschikbaar bij de ingang. Neem een kijkje en maak je keuze.",
"Kan ik je helpen bij het kiezen van een gerecht? Hier zijn de beschikbare opties.",
"Ja, we hebben een menukaart met speciale dieetopties. Hier is het voor je.",
"Laat me je de menu-opties en prijzen tonen.",
"Natuurlijk, hier is de menukaart om je te helpen bij je keuze.",
"Hier zijn de specialiteiten van het huis. Neem een kijkje op de menukaart.",
"Ja, je kunt de menukaart bekijken voordat je je keuze maakt.",
"Zeker, we hebben ook een menukaart met kindermenu-opties.",
"Uiteraard, hier is de menukaart. Neem je tijd om je keuze te maken.",
"Zou je ook graag de lijst met ingrediënten willen zien? Hier is de menukaart.",
"Hier zijn de beschikbare gerechten waaruit je kunt kiezen.",
"Onze menukaart bevat ook seizoensgebonden gerechten. Hier is het voor je.",
"Ja, je kunt de menukaart raadplegen om je dieetvoorkeuren te controleren.",
"Hier is de lijst met vegetarische gerechten die we aanbieden.",
"We hebben ook veganistische opties op onze menukaart. Laat me het je tonen.",
"Natuurlijk, ik kan je de menu-opties en aanbevelingen geven.",
"Alsjeblieft, hier is de menukaart. Neem rustig de tijd om je maaltijd te kiezen.",
"Natuurlijk, hier is de lijst met drankjes die we serveren.",
"Onze populairste gerechten staan op het menu aangegeven. Laat me je adviseren.",
"Ja, we hebben gezonde opties op het menu. Laat me ze je tonen."
]
dietwensen_responses = [
"Hallo, heeft u speciale dieetwensen waar we rekening mee moeten houden?",

]
