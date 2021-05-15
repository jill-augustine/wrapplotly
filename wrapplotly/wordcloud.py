from wordcloud import WordCloud
import PIL
import re
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
from wrapplotly.util import as_list

wc = WordCloud(font_path = '/Library/Fonts/Microsoft/Arial.ttf', prefer_horizontal = 0.2, random_state=89860).generate_from_frequencies({'hi':5, 'lo': 1, 'medium':3})
plt.imshow(wc)
plt.show()

dir(plt.imshow(wc))
[w for w in dir(plt.imshow(wc).axes) if 'lim' in w]
plt.imshow(wc).axes.get_xlim()
plt.imshow(wc).axes.get_ylim()

for item in wc.layout_:
    print(item)

unnested = [dict(text = text, freq = freq, fontsize = fontsize, x = col, y = row, orientation = orientation, color = color)
            for (text, freq), fontsize, (row, col), orientation, color in wc.layout_]

font_obj = PIL.ImageFont.truetype(wc.font_path, 16)
font_family = as_list(font_obj.getname())[0]
font_obj.getsize('hi')

#f = PIL.ImageFont.truetype(wc.font_path)
#f.getname() #('Droid Sans Mono', 'Regular')

calculate_centers = True
# default for now is False
calculate_centers = False if calculate_centers is None else calculate_centers
fig = go.Figure()
for word in unnested[1:2]:
    if word['orientation'] is None:
        textangle = 0
    else:
        textangle = 270

    #text = word['text']
    #xanchor = 'left'
    #yanchor = 'top' # might change if we flip the y-axis
    #showarrow = False
    anchor_point = np.array([word['x'],word['y']])
    if calculate_centers:
        # create font object
        font = PIL.ImageFont.truetype(wc.font_path, word['fontsize'])
        # transpose font object
        font = PIL.ImageFont.TransposedFont(font, orientation=word['orientation'])
        box_size = np.array(font_obj.getsize(word['text'])) + wc.margin // 2
        # shift anchor point to the centre of the text
        anchor_point = anchor_point + (box_size / 2)
        
    #font_dict = dict(size = word['fontsize'] * 2.2,
    #            color = word['col'],
    #            family = font_family+', sans-serif')
    hovertext = ('<b>Word:</b> {}<br><b>Relative Frequency:</b> {}'
                 .format(word['text'], word['freq']))
    hoverlabel = dict(bgcolor = word['color'],
                      bordercolor = wc.background_color,
                      font_family = font_family+', sans-serif',
                      font_color = wc.background_color
                      )
    fig = fig.add_annotation(text = '',
                       x = anchor_point[0],
                       y = anchor_point[1],
                       #borderpad = wc.margin,
                       #textangle = textangle,
                       #font = font_dict,
                       hovertext = hovertext,
                       hoverlabel = hoverlabel,
                       xanchor = 'left',
                       yanchor = 'top',
                       showarrow = False)

x_max = wc.width
y_max = wc.height
fig = fig.update_layout(yaxis_showgrid = False, xaxis_showgrid = False, 
                        yaxis_zeroline = False, xaxis_zeroline = False,
                        yaxis_range = [wc.height,0], yaxis_constrain = 'domain',
                        yaxis_scaleanchor = 'x', yaxis_scaleratio = 1,
                        xaxis_range = [0,wc.width], xaxis_constrain = 'domain',
                        plot_bgcolor = wc.background_color,
                        #paper_bgcolor = wc.background_color
                        xaxis_showticklabels = False,
                        yaxis_showticklabels = False
                        )
fig.show()


[attr for attr in dir(wc) if re.search('_$', attr) is not None]
wc.layout_
wc.words_

# create image
img_grey = PIL.Image.new("L", (wc.width, wc.height))
draw = PIL.ImageDraw.Draw(img_grey)
img_array = np.asarray(img_grey)
font_sizes, positions, orientations, colors = [], [], [], []
font_obj = PIL.ImageFont.truetype(wc.font_path, 16)
transposed_font_obj = PIL.ImageFont.TransposedFont(font_obj, PIL.Image.ROTATE_90)
draw.textsize('medium', font=font_obj)
draw.textsize('medium', font=transposed_font_obj)

font_obj.getsize('medium')
np.array(font_obj.getsize('medium')) + wc.margin // 2


type(PIL.Image.ROTATE_180)

a = np.diag(np.arange(6))
np.cumsum(a, axis = 1)
np.cumsum(np.cumsum(1 * a, axis=1),axis=0).astype(np.uint32)