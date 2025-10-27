from pygame.time import Clock

class Time:
    _delta_time = 0
    _clock = Clock()

    desired_frame_rate = 60.0

    def tick():
        Time._delta_time = Time._clock.tick(Time.desired_frame_rate)
    
    def get_delta_time():
        return Time._delta_time