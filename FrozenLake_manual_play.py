import gym 
import colorama as cr
import msvcrt

cr.init(autoreset=True)
def getkey():
    return msvcrt.getch().decode('utf-8').lower()


#register Frozen lake with is_slippery false
gym.envs.registration.register(
    id='FrozenLake-v00',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name':'4x4','is_slippery':False}
)

env=gym.make('FrozenLake-v00') #위 아이디와 같이 해주어야함
env.render() #show initial board

while True:
    key=msvcrt.getch().decode('utf-8').lower()
    if key not in ['w','a','s','d']: #방향키 말고 다른 키 누를 시
        print("Game aborted!")
        break 
    else:
        if key=='s':
            action=1
        elif key=='a':
            action=0
        elif key=='d':
            action=2
        elif key=='w':
            action=3

    state,reward,done,info=env.step(action)
    env.render() #show board after action /similar to flip 
    print("State: ",state,"Action:",action,"Reward: ",reward,"Info: ",info)
    if done:
        print("Finished with reward",reward)
        break
    



