
__all__ = ['format_canvas_axes', 'create_canvas', 'create_ratio_canvas', 'format_ratio_canvas_axes']

from ROOT import TCanvas, TPad
import ROOT
import rootplotlib as rpl


def create_canvas(name: str,
                  title: str ="",
                  canw: int=700,
                  canh: int=500 ) -> rpl.Figure:
    """
    Creates a Figure object with the given canvas parameters

    Parameters
    ----------
    name : str
        Canvas name
    title : str, optional
        Canvas title, by default ""
    canw : int, optional
        Canvas width as defined by ROOT.TCanvas, by default 700
    canh : int, optional
        Canvas height as defined by ROOT.TCanvas, by default 500

    Returns
    -------
    rpl.Figure
        _description_
    """
    canvas = TCanvas( name, title, canw, canh )
    fig = rpl.Figure(canvas)
    rpl.set_figure(fig)
    return fig

def create_ratio_canvas(name: str,
                        title: str="",
                        canw: int=700,
                        canh: int=500,
                        ratio_size_as_fraction: float=0.35,
                        drawopt: str='pE1') -> rpl.Figure:
    """
    Creates a Figure object with a canvas with two pads:
    - A bigger one on top named pad_top
    - A smaller one on the bottom named pad_bot

    Parameters
    ----------
    name : str
        Canvas name
    title : str, optional
        Canvas title, by default ""
    canw : int, optional
        Canvas width as defined by ROOT.TCanvas, by default 700
    canh : int, optional
        Canvas height as defined by ROOT.TCanvas, by default 500
    ratio_size_as_fraction : float, optional
        Pecentage of canvas vertical size occuppied by the
        bottom pad, by default 0.35
    drawopt : str, optional
        ROOT draw operation, by default 'pE1'

    Returns
    -------
    rpl.Figure
        Rootplotlib figure with the canvas created
    """

    canvas = ROOT.TCanvas(name,title,canw,canh)
    fig = rpl.Figure(canvas)
    rpl.set_figure(fig)
    canvas.SetFillStyle(4050)

    # Top
    canvas.cd()
    top = ROOT.TPad("pad_top",
                    "This is the top pad",
                    0.0,ratio_size_as_fraction,1.0,1.0)
    top.SetBottomMargin(0.02/float(top.GetHNDC()))
    top.SetTopMargin(0.04/float(top.GetHNDC()))
    top.SetRightMargin(0.05)
    top.SetLeftMargin(0.16)
    top.SetFillColor(0)
    top.Draw(drawopt)
    fig.append(top)

    # Bot
    canvas.cd()
    bot = ROOT.TPad("pad_bot",
                    "This is the bottom pad",
                    0.0,0.0,1.0,ratio_size_as_fraction)
    bot.SetBottomMargin(0.12/float(bot.GetHNDC()))
    bot.SetTopMargin(0.02/float(bot.GetHNDC()))
    bot.SetRightMargin(0.05)
    bot.SetLeftMargin(0.16)
    bot.SetFillColor(0)
    bot.Draw(drawopt)
    fig.append(bot)
    
    return fig



def format_canvas_axes(  XTitleSize   = 22
                        ,XTitleOffset = 0.98
                        ,XTitleFont   = 43
                        ,XLabelSize   = 22
                        ,XLabelOffset = 0.002
                        ,XLabelFont   = 43
                        ,XNDiv = None

                        ,YTitleSize   = 22
                        ,YTitleOffset = 1.75
                        ,YTitleFont   = 43
                        ,YLabelSize   = 22
                        ,YLabelOffset = 0.006
                        ,YLabelFont   = 43
                        ,YNDiv = [10,5,0]

                        ,ZTitleSize   = 22
                        ,ZTitleOffset = 0.85
                        ,ZTitleFont   = 43
                        ,ZLabelSize   = 22
                        ,ZLabelOffset = 0.002
                        ,ZLabelFont   = 43
                        ,pad = None
                        ,fig = None
                        ) :
    
    if fig is None:
        fig = rpl.get_figure()
    canvas = fig.get_pad(pad)

    for primitive in canvas.GetListOfPrimitives() :
        if not hasattr(primitive,'GetXaxis') :
            continue
        primitive.GetXaxis().SetTitleSize  (XTitleSize  )
        primitive.GetXaxis().SetTitleOffset(XTitleOffset/float(canvas.GetHNDC()))
        primitive.GetXaxis().SetTitleFont  (XTitleFont  )
        primitive.GetXaxis().SetLabelSize  (XLabelSize  )
        primitive.GetXaxis().SetLabelOffset(XLabelOffset/float(canvas.GetHNDC()))
        primitive.GetXaxis().SetLabelFont  (XLabelFont  )
        primitive.GetXaxis().SetTickLength(0.02/float(canvas.GetHNDC()))
        if XNDiv:
            primitive.GetXaxis().SetNdivisions (XNDiv[0],XNDiv[1],XNDiv[2])
        primitive.GetYaxis().SetTitleSize  (YTitleSize  )
        primitive.GetYaxis().SetTitleOffset(YTitleOffset)
        primitive.GetYaxis().SetTitleFont  (YTitleFont  )
        primitive.GetYaxis().SetLabelSize  (YLabelSize  )
        primitive.GetYaxis().SetLabelOffset(YLabelOffset)
        primitive.GetYaxis().SetLabelFont  (YLabelFont  )
        primitive.GetYaxis().SetNdivisions (YNDiv[0],YNDiv[1],YNDiv[2])
        if not hasattr(primitive,'GetZaxis') :
            continue
        primitive.GetZaxis().SetTitleSize  (ZTitleSize  )
        primitive.GetZaxis().SetTitleOffset(ZTitleOffset)
        primitive.GetZaxis().SetTitleFont  (ZTitleFont  )
        primitive.GetZaxis().SetLabelSize  (ZLabelSize  )
        primitive.GetZaxis().SetLabelOffset(ZLabelOffset)
        primitive.GetZaxis().SetLabelFont  (ZLabelFont  )
        # if here, we setup x, y and z axis
        break
    canvas.Modified()
    canvas.Update()




def format_ratio_canvas_axes(  XTitleSize   = 22
                              ,XTitleOffset = 0.98
                              ,XTitleFont   = 43
                              ,XLabelSize   = 22
                              ,XLabelOffset = 0.002
                              ,XLabelFont   = 43
      
                              ,YTitleSize   = 22
                              ,YTitleOffset = 1.75
                              ,YTitleFont   = 43
                              ,YLabelSize   = 22
                              ,YLabelOffset = 0.006
                              ,YLabelFont   = 43
                              ,YNDiv = [10,5,0]
      
                              ,ZTitleSize   = 22
                              ,ZTitleOffset = 0.85
                              ,ZTitleFont   = 43
                              ,ZLabelSize   = 22
                              ,ZLabelOffset = 0.002
                              ,ZLabelFont   = 43
                              ,fig = None
                              ) :

       
    format_canvas_axes(fig=fig, pad='pad_top',XLabelOffset=0.1
                     ,XTitleSize=XTitleSize,XTitleOffset=XTitleOffset,XTitleFont=XTitleFont
                     ,XLabelSize=XLabelSize,XLabelFont=XLabelFont
                     ,YTitleSize=YTitleSize,YTitleOffset=YTitleOffset,YTitleFont=YTitleFont
                     ,YLabelSize=YLabelSize,YLabelOffset=YLabelOffset,YLabelFont=YLabelFont
                     ,YNDiv=YNDiv
                     ,ZTitleSize=ZTitleSize,ZTitleOffset=ZTitleOffset,ZTitleFont=ZTitleFont
                     ,ZLabelSize=ZLabelSize,ZLabelOffset=ZLabelOffset,ZLabelFont=ZLabelFont
                      )
    format_canvas_axes(fig=fig, pad='pad_bot',YLabelOffset=0.009
                     ,XTitleSize=XTitleSize,XTitleOffset=XTitleOffset,XTitleFont=XTitleFont
                     ,XLabelSize=XLabelSize,XLabelOffset=XLabelOffset,XLabelFont=XLabelFont
                     ,YTitleSize=YTitleSize,YTitleOffset=YTitleOffset,YTitleFont=YTitleFont
                     ,YLabelSize=YLabelSize,YLabelFont=YLabelFont
                     ,YNDiv = [5,5,0]
                     ,ZTitleSize=ZTitleSize,ZTitleOffset=ZTitleOffset,ZTitleFont=ZTitleFont
                     ,ZLabelSize=ZLabelSize,ZLabelOffset=ZLabelOffset,ZLabelFont=ZLabelFont
                     )


def savefig( output ):
    fig = rpl.get_figure()
    fig.savefig(output)