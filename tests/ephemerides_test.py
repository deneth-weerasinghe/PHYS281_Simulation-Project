import jplephem
from spiceypy import sxform, mxvg
from poliastro import constants
from astropy.time import Time
from astropy.coordinates import get_body_barycentric_posvel
import astropy.constants

bodies = ["Sun", "Mercury", "Venus", "Earth-Moon-barycenter", "Earth", "Moon", "Mars", "Jupiter", "Saturn", "Uranus",
          "Neptune", "Pluto"]

t = Time("2021-12-04 00:00:00.0", scale="tdb")

sun_pos, sun_vel = get_body_barycentric_posvel(bodies[0].lower(), t, ephemeris="jpl")

state_vec = [
    sun_pos.xyz[0].to("m").value,
    sun_pos.xyz[0].to("m").value,
    sun_pos.xyz[0].to("m").value,
    sun_vel.xyz[0].to("m/s").value,
    sun_vel.xyz[0].to("m/s").value,
    sun_vel.xyz[0].to("m/s").value,
]

#  get transformation matrix to the ecliptic (use time in Julian days)
transform = sxform("J2000", "ECLIPJ2000", t.jd)

#  transform state vector to ecliptic
state_vec_ec = mxvg(transform, state_vec, 6, 6)

#  positions and velocities
position = [state_vec_ec[0], state_vec_ec[1], state_vec_ec[2]]  # FINAL VALUE
velocity = [state_vec_ec[3], state_vec_ec[4], state_vec_ec[5]]  # FINAL VALUE

# mass
mass = (constants.GM_sun / astropy.constants.G).value  # FINAL VALUE

print(position)
print(mass)
