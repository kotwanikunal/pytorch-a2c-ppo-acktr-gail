import cv2

class Config:
    def __init__(self):
        self.threshold = 0.8 #TODO Should be set for each method. 0.8 is for CCOEFF_NORMED
        self._templates = {
            'mario_frwrd' :{  'path':'ob_detection/images/templates/mario_forward.png',
                        'color': (255, 255, 255),
                        'threshold': self.threshold,
                        },
            'mario_backwrd' :{  'path':'ob_detection/images/templates/mario_backward.png',
                        'color': (255, 255, 255),
                        'threshold': self.threshold,
                        },
            'mario_big_left': {'path': 'ob_detection/images/templates/mario_big_left.png',
                               'color': (255, 255, 255),
                               'threshold': self.threshold,
                               },
            'mario_big_left_squeezed': {'path': 'ob_detection/images/templates/mario_big_left_squeezed.png',
                                        'color': (255, 255, 255),
                                        'threshold': self.threshold,
                                        },
            'mario_big_right_squeezed': {'path': 'ob_detection/images/templates/mario_big_right_squeezed.png',
                                         'color': (255, 255, 255),
                                         'threshold': self.threshold,
                                         },
            'mario_big_right': {'path': 'ob_detection/images/templates/mario_big_right.png',
                                'color': (255, 255, 255),
                                'threshold': self.threshold,
                                },
            'mario_fire_left': {'path': 'ob_detection/images/templates/mario_fire_left.png',
                                'color': (255, 255, 255),
                                'threshold': self.threshold,
                                },
            'mario_fire_right': {'path': 'ob_detection/images/templates/mario_fire_right.png',
                                 'color': (255, 255, 255),
                                 'threshold': self.threshold,
                                 },
            'enemy1':{  'path':'ob_detection/images/templates/enemy1.png',
                        'color': (153, 153, 153),
                        'threshold': self.threshold,
                        },
            'enemy2': {'path': 'ob_detection/images/templates/enemy2.png',
                       'color': (153, 153, 153),
                       'threshold': self.threshold,
                       },
            'obs1'  :{  'path':'ob_detection/images/templates/obs1.png',
                        'color':  (77, 77, 77),
                        'threshold': self.threshold,
                        },
            'obs3'  :{  'path':'ob_detection/images/templates/obs3.png',
                        'color':  (77, 77, 77),
                        'threshold': self.threshold,
                        },
            'obs2'  :{  'path':'ob_detection/images/templates/obs2.png',
                        'color':  (77, 77, 77),
                        'threshold': self.threshold,
                        },
            'obs4': {'path': 'ob_detection/images/templates/obs4_pipe_top.png',
                     'color': (77, 77, 77),
                     'threshold': self.threshold,
                     },
            'obs5': {'path': 'ob_detection/images/templates/obs5_pipe_body.png',
                     'color': (77, 77, 77),
                     'threshold': self.threshold,
                     },
            'brick' :{  'path':'ob_detection/images/templates/brick.png',
                        'color':  (77, 77, 77),
                        'threshold': self.threshold,
                        },
            'brick2': {'path': 'ob_detection/images/templates/brick2.png',
                       'color': (77, 77, 77),
                       'threshold': self.threshold,
                       },
        }

        self.methods = {
            'CCOEFF':cv2.TM_CCOEFF, 
            'CCOEFF_NORMED':cv2.TM_CCOEFF_NORMED, 
            'CCORR':cv2.TM_CCORR,
            'CCORR_NORMED':cv2.TM_CCORR_NORMED, 
            'SQDIFF':cv2.TM_SQDIFF, 
            'SQDIFF_NORMED':cv2.TM_SQDIFF_NORMED
        }

        #To be used outside the class
        self.templates = None
        self.colors = None
        self.method = self.methods['CCOEFF_NORMED']
    
    def get_templates(self):
        '''
        Return template images corresponding to all templates defined in _templates
        '''
        if self.templates:
            return self.templates

        #Initialize template images from template definitions
        self.templates = {name: template['path'] for name, template in self._templates.items()}
        return self.templates
    
    def get_colors(self):
        '''
        Return colors to be filled(for each template defined in _templates) when a template match is detected in a frame 
        '''
        if self.colors:
            return self.colors
        
        #Initialize colors from template definitions
        self.colors = {name: template['color'] for name, template in self._templates.items()}
        return self.colors
    
    def get_method(self):
        return self.method
