#6music.py

 

class vol_control:

    def __init__(self):

        self.play_volume=5

 

    def change_vol(self,vol):

        if (vol >20):

            print ('too high volume ....cannot take it...setting it back to 5')

        else:           

            self.play_volume = vol

       

    def disp_vol(self):

        print ('it is playing in volume unit ',self.play_volume)

       

class music_player:

    def __init__(self):

        self.play_type = 'from song 1 to song 10'

       

    def disp(self):

        print ('my music system plays ',self.play_type)       

        

# some team guy Kumar

class my_own_music_player(music_player):

    def __init__(self,mystyle_of_play):

        super().__init__()

        self.play_type = mystyle_of_play

        self.vc = vol_control()   # HAS A , aggregation

   

    def disp(self):

        print ('well WATCH my music system plays ',self.play_type) 

        self.vc.change_vol(19)             

        self.vc.disp_vol()

 

# some team guy Ravi Kamath

class my_own_music_player_1(music_player):

    def __init__(self,mystyle_of_play,beats):

        super().__init__()

        self.play_type = mystyle_of_play

        self.beats = beats

        self.vc = vol_control()   # HAS A , aggregation

    '''

    def disp(self):

        print ('well WATCH my music system plays ',self.play_type)

        print ('music using the beats type ',self.beats)

        self.vc.disp_vol()       

    ''' 

print ('i am in main block')       

 

m1 = music_player()

m1.disp()

print ('--------------')

 

print ('------Kumar ---------')

my_own1 = my_own_music_player('shuffle the songs and play random ')

my_own1.disp()

 

print ('------Ravi Kamath ---------')

my_ravi_own = my_own_music_player_1('only 15 songs from last to first from Paylist-A','beat type ABC')

my_ravi_own.disp()

print ('--------------')

 