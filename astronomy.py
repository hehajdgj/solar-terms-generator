from dataclasses import dataclass
from skyfield.api import load
from skyfield import almanac
from skyfield import almanac_east_asia as almanac_ea
from skyfield.timelib import Time

@dataclass
class SolarTerm:
    """A clean container holding the raw astronomical data for a single term."""
    term_index: int
    time: Time

    @property
    def epoch(self) -> int:
        """Returns the universal UNIX timestamp."""
        return int(self.time.utc_datetime().timestamp())

def calculate_astronomy(start_year, end_year):
    """
    Runs the Skyfield orbital math exactly once.
    Returns a list of raw SolarTerm objects.
    """
    # Load the planetary ephemeris data and timescale
    eph = load('de421.bsp')
    ts = load.timescale()
    
    # Define our time window
    t0 = ts.utc(start_year, 1, 1)
    t1 = ts.utc(end_year + 1, 1, 1)
    
    # Run the discrete solver
    t, tm = almanac.find_discrete(t0, t1, almanac_ea.solar_terms(eph))
    
    # Zip the arrays together and pack them into the dataclass
    return [SolarTerm(term_index=int(tmi), time=ti) for tmi, ti in zip(tm, t)]