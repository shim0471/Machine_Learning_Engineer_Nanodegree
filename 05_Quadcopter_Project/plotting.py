import numpy as np
import matplotlib.pyplot as plt

def plotting(results, standalone=True):
    if standalone:
        plt.subplots(figsize=(15, 15))
        
    plt.subplot(3, 3, 1)
    plt.title('Reward')
    plt.plot(results['episode'], results['total_reward'], label='Reward')
    plt.xlabel('Episode')
    plt.ylabel('Total reward')
    plt.grid(True)    

    plt.subplot(3, 3, 2)
    plt.title('Position')
    plt.plot(results['episode'], results['x'], label='x')
    plt.plot(results['episode'], results['y'], label='y')
    plt.plot(results['episode'], results['z'], label='z')
    plt.xlabel('Episode')
    plt.ylabel('Position')
    plt.grid(True)
    if standalone:
        plt.legend()

    plt.subplot(3, 3, 3)
    plt.title('Velocity')
    plt.plot(results['time'], results['x_velocity'], label='x')
    plt.plot(results['time'], results['y_velocity'], label='y')
    plt.plot(results['time'], results['z_velocity'], label='z')
    plt.xlabel('Time_second')
    plt.ylabel('Velocity')
    plt.grid(True)
    if standalone:
        plt.legend()

    plt.subplot(3, 3, 4)
    plt.title('Euler')
    plt.plot(results['time'], results['phi'], label='phi')
    plt.plot(results['time'], results['theta'], label='theta')
    plt.plot(results['time'], results['psi'], label='psi')
    plt.xlabel('Time_second')
    plt.ylabel('Euler_angle')
    plt.grid(True)
    if standalone:
        plt.legend()

    plt.subplot(3, 3, 5)
    plt.title('Euler Velocity')
    plt.plot(results['time'], results['phi_velocity'], label='phi')
    plt.plot(results['time'], results['theta_velocity'], label='theta')
    plt.plot(results['time'], results['psi_velocity'], label='psi')
    plt.xlabel('Episode')
    plt.ylabel('Euler_velocity')
    plt.grid(True)
    if standalone:
        plt.legend()

    plt.subplot(3, 3, 6)
    plt.title('Rotor Speed')
    plt.plot(results['time'], results['rotor_speed1'], label='Rotor 1')
    plt.plot(results['time'], results['rotor_speed2'], label='Rotor 2')
    plt.plot(results['time'], results['rotor_speed3'], label='Rotor 3')
    plt.plot(results['time'], results['rotor_speed4'], label='Rotor 4')
    plt.xlabel('Time_second')
    plt.ylabel('Rotor Speed')
    plt.grid(True)
    if standalone:
        plt.legend()

        
    if standalone:
        plt.tight_layout()
        plt.show()