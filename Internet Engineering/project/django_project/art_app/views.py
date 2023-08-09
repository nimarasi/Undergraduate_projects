"""
we write some functions here which will automatically invoked by the url.py in /django_project/urls that when a http request comes
to the certain url a function from view.py will invoked to render a special content
"""
from django.shortcuts import render


# Create your views here.

# my defined functions
def starting_page(request):
    return render(request , "art_app/starting_page.html" , {
        "show" : True})#request --> input parameter of def
    
def art_fields(request):
    """
    input parameter of fincton will automatically provided by django
    """
    list_art_fields = [{
        'title' : 'Persian traditional music',
        'slug' : 'a-first-field',
        'text' : "Persian traditional music or Iranian traditional music, also known as Persian classical music or Iranian classical music,refers to the classical music of Iran (also known as Persia).\
              It consists of characteristics developed through the country's \
              classical, medieval, and contemporary eras. It also influenced areas and regions that are considered part of Greater Iran.",
        'img' : '../../../static/art_app/styles/images/7.jpg'
    },
    {
        'title' : 'Painting',
        'slug' : 'a-second-field',
        'text' : "Painting is the practice of applying paint, pigment, color or other medium to a solid surface.The medium is commonly applied to the base with a brush, but other implements, such as knives, sponges, and airbrushes, can be used.\
                    In art, the term painting describes both the act and the result of the action (the final work is called 'a painting'). The support for paintings includes such surfaces as walls, paper, canvas, wood, glass, lacquer, pottery, leaf,\
                    copper and concrete, and the painting may incorporate multiple other materials, including sand, clay, paper, plaster, gold leaf, and even whole objects.",
        'img' : '../../../static/art_app/styles/images/8.jpg'
    },
    {
        'title' : 'Photography',
        'slug' : 'a-third-field',
        'text' : " Photography is the art, application, and practice of creating durable images by recording light, either electronically by means of an image sensor, or chemically by means of a light-sensitive material such as photographic  \
                    film. It is employed in many fields of science, manufacturing (e.g., photolithography), and business, as well as its more direct uses for art, film and video production, recreational purposes, hobby, and mass communication.",
        'img' : '../../../static/art_app/styles/images/9.jpg'
    }]
    return render(request , "art_app/art_fields.html" , {
        'show_fields' : True,
        "art_fields" : list_art_fields}) # request --> input parameter of def



def fields_detail(request , field_detail):
    print(field_detail)
    if field_detail == 'a-first-field':
        print('yessssssssssssss')
        selected_field_details = {
                            'title':'Details and celebrities of the field',
                            'celebrity' : 'Mohammad Reza Shajarian',
                            'description' : "Mohammad-Reza Shajarian (Persian: محمدرضا شجريان; Persian pronunciation: [mohæmːæd ɾeˈzɒː ʃædʒæɾiˈɒːn], 23 September 1940 – 8 October 2020) was an Iranian singer and master (Ostad) of Persian traditional music. \
                                            He was also known for his skills in Persian calligraphy and humanitarian activities.\
                                            Shajarian started his singing career in 1959 at Radio Khorasan, rising to prominence in the 1960s with his distinct singing style.\
                                            His main teachers were Ahmad Ebadi, Esmaeil Mehrtash, Abdollah Davami, and Nour-Ali Boroumand. He also learned the vocal styles of singers from previous generations, including Reza Gholi Mirza Zelli, Fariborz Manouchehri, Ghamar Molouk Vaziri, Eghbal Azar, and Taj Isfahani. He has cited legendary Persian tar soloist Jalil Shahnaz as highly influential to his development, \
                                            indicating that he has often tried to mimic Shahnaz's playing style in his singing. ",
                            'img' : '../../static/art_app/styles/images/10.jpg'
                        }
    elif field_detail == 'a-second-field':
       
        selected_field_details = {
                            'title':'Details and celebrities of the field',
                            'celebrity' : 'Leonardo da Vinci',
                            'description' : "Leonardo di ser Piero da Vinci[b] (15 April 1452 – 2 May 1519) was an Italian polymath of the High Renaissance who was active as a painter, draughtsman, engineer, scientist, theorist, sculptor, and architect. While his fame initially rested on his achievements \
                                            as a painter, he also became known for his notebooks, in which he made drawings and notes on a variety of subjects, including anatomy, astronomy, botany, cartography, painting, and paleontology.\
                                            Leonardo is widely regarded to have been a genius who epitomized the Renaissance humanist ideal, and his collective works comprise a contribution to later generations of artists matched only by that of his younger contemporary, Michelangelo. \
                                            The Mona Lisa (/ˌmoʊnə ˈliːsə/ MOH-nə LEE-sə; Italian: Gioconda [dʒoˈkonda] or Monna Lisa [ˈmɔnna ˈliːza]; French: Joconde [ʒɔkɔ̃d]) is a half-length portrait painting by Italian artist Leonardo da Vinci. \
                                            Considered an archetypal masterpiece of the Italian Renaissance, it has been described as 'the best known, the most visited, the most written about, the most sung about, the most parodied work of art in the world'. \
                                            The painting's novel qualities include the subject's enigmatic expression, the monumentality of the composition, the subtle modelling of forms, and the atmospheric illusionism.",
                            'img' : '../../static/art_app/styles/images/11.jpg'
                        }
    else:
         selected_field_details = {
                            'title':'Details and celebrities of the field',
                            'celebrity' : 'Cynthia Morris Sherman',
                            'description' : "Cynthia Morris Sherman (born January 19, 1954) is an American artist whose work consists primarily of photographic self-portraits, depicting herself in many different contexts and as various imagined characters.\
                                            Her breakthrough work is often considered to be the collected Untitled Film Stills, a series of 70 black-and-white photographs of herself evoking typical female roles in performance media (especially arthouse films and popular B-movies). In the 1980s, she used color film and large prints, and focused more on costume, lighting and facial expression.",
                            'img' : '../../static/art_app/styles/images/12.jpg'
                        }

    return render(request , 'art_app/fields_detail.html',{
            'field_title' : selected_field_details['title'], 
            'field_celebrity' : selected_field_details['celebrity'], 
            'field_description' : selected_field_details['description'],
            'field_img' : selected_field_details['img']
            })
    