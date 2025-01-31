class Piece:
  
  def __init__(self, color, type, image, takeable = False):
    self.color = color
    self.type = type
    self.takeable = takeable
    self.image = image