#handles most of the logic and data for the television to work.

class Television:
    """
    A class that provides variables for some of the functions of the TV.
    """
    #controls the volume range, and the channel range.
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 20
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 5

    #Dictionary handling the channels names and display images
    CHANNEL_DATA = {
        0: {"name": "MAJOR NEWS - BREAKING NOW ", "image": "images/news.jpg"},
        1: {"name": "FOOD NETWORK", "image": "images/food.jfif"},
        2: {"name": "Horror Movie: The Reaper", "image": "images/horror_movie.jpg"},
        3: {"name": "SPORTS: THE LAST DANCE", "image": "images/cool.jpg"},
        4: {"name": "SCIENCE CHANNEL: Proteins ", "image": "images/science.png"},
        5: {"name": "ANIMAL PLANET", "image": "images/nature.jpg"},
    }

    def __init__(self)-> None:
        """
        Normal init function. Sets the TV default settings based on Class Television variables.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    #controls power status on or off using boolean values.
    def power(self)-> None:
        """
        Turns TV ON or OFF through boolean value swapping.
        """
        self.__status = not self.__status

    #controls the mute status, only if TV is on
    def mute(self)-> None:
        """
        Mutes or unmutes the TV through boolean value swapping.
        """
        if self.__status == True:

            self.__muted = not self.__muted

    #controls the channel up, only if TV is on.
    def channel_up(self)-> None:
        """
        If TV is powered on, increment by 1.
        Loops back to MIN_CHANNEL, if current position is equal to MAX_CHANNEL.
        """
        if self.__status == True:

            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

            else:
                self.__channel += 1

    # controls the channel down, only if TV is on.
    def channel_down(self)-> None:
        """
        If TV is powered on, decrement by 1.
        Loops back to MAX_CHANNEL, if current position is equal to MIN_CHANNEL.
        """
        if self.__status == True:

            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

            else:
                self.__channel -= 1

    # controls the volume up, only if TV is on.
    def volume_up(self)-> None:
        """
        If TV is on: unmute TV and increment by 1.
        """
        if self.__status == True:

            if self.__muted == True:
                self.__muted = False

            if self.__volume != Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self)-> None:
        """
        If TV is on decrement volume by 1 and unmute the TV.
        :return:
        """
        if self.__status == True:

            if self.__muted == True:
                self.__muted = False

            if self.__volume != Television.MIN_VOLUME:
                self.__volume -= 1

    def get_status(self) -> dict:
        """
        Contains a dictionary of different the different status states of the TV itself.
        :return:
        """
        return {
            "status": self.__status,
            "muted": self.__muted,
            "volume": self.__volume,
            "channel": self.__channel,
            "channel_data": self.CHANNEL_DATA.get(self.__channel, {"name": "Unknown Channel", "image": None}),
        }