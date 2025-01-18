import pandas as pd

# list of seed data
seed_profiles_list = [
    ['COR TIN', 'Plains Coreopsis', 'Coreopsis Tinctoria', 'ANN', 'EAS', 'FU', 'MO'],
    ['PRO PAR', 'Devil\'s Claw', 'Proboscidea Parviflora', 'ANN', 'MED', 'FP', 'LM'],
    ['BOU CUR', 'Side Oats Gramma', 'Bouteloua Curtipendula', 'GRA', 'EAS', 'FP', 'LO'],
    ['HIL RIG', 'Big Galleta Grass', 'Hilaria Rigda', 'GRA', 'EAS', 'FU', 'LO'],
    ['CON GRE', 'Gregg\'s Mistflower', 'Concoclinium Greggi', 'GRO', 'EAS', 'PA', 'MO'],
    ['BAH PAR', 'Parish\'s Goldeneye', 'Bahiopsis Parishii', 'SHR', 'EAS', 'FU', 'LM'],
    ['VAU CAL', 'Arizona Rosewood', 'Vauquelinia Californica', 'SHR', 'EAS', 'FP', 'LO'],
    ['ABU PAL', 'Superstition Mallow', 'Abutilon Palmeri', 'SHR', 'EAS', 'FU', 'LO'],
    ['ENC FAR', 'Brittlebush', 'Encelia Farinosa var Phenicodonta', 'SHR', 'EAS', 'FU', 'VL'],
    ['DOD VIS', 'Hopbush', 'Dodonaea Viscosa', 'SHR', 'MED', 'FU', 'LO'],
    ['CAL ERI', 'Pink Fairy Duster', 'Calliandra Eriphylla', 'SHR', 'MED', 'FU', 'LO'],
    ['ACO WRI', 'Pink Perezia', 'Acourtia Wrightii', 'SHR', 'UNK', 'PA', 'MO'],
    ['ABU INC', 'Pelotazo', 'Abutilon Incanum', 'SHR', 'UNK', 'FU', 'LO'],
    ['BEB JUN', 'Rough Sweetbush', 'Bebbia Juncea Aspera', 'SHR', 'EAS', 'FP', 'LO'],
    ['SPH AMB', 'Desert Globemallow', 'Sphaeralcea Ambigua', 'SHR', 'EAS', 'FU', 'VL'],
    ['GOS THU', 'Wild Cotton', 'Gossypium Thurberi', 'SHR', 'UNK', 'FP', 'LO'],
    ['THY PEN', 'Paralenna', 'Thymophylia Pentachaeta', 'SUB', 'EAS', 'FP', 'LO'],
    ['ERI DIV', 'Spreading Daisy', 'Erigeron Divergens', 'SUB', 'EAS', 'FP', 'LO'],
    ['SEN COV', 'Desert Senna', 'Senna Covesii', 'SUB', 'EAS', 'FU', 'VL'],
    ['PRO VEL', 'Velvet Mesquite', 'Prosopis Velutina', 'TRE', 'MED', 'FU', 'LO'],
    ['PAR FLO', 'Blue Paloverde', 'Parkinsonia Florida', 'TRE', 'DIF', 'FU', 'LO'],
    ['STR ODO', 'Screwbean Mesquite', 'Strombocarpa Odorata', 'TRE', 'EAS', 'UNK', 'LO'],
    ['CHI LIN', 'Desert Willow', 'Chilopsis Linearis', 'TRE', 'EAS', 'FU', 'LO'],
    ['CHI LIN ARC', 'Native Desert Willow', 'Chilopsis Linearis Arcuata', 'TRE', 'EAS', 'FU', 'LO'],
    ['OLN TES', 'Ironwood', 'Olneya Tesota', 'TRE', 'MED', 'FU', 'LO'],
    ['PAR MIC', 'Foothills Palo Verde', 'Parkinsonia Microphylla', 'TRE', 'DIF', 'FU', 'LO'],
    ['GAI SP', 'Blanketflower', 'Gaillardia Aristata', 'PER', 'EAS', 'FP', 'LM'],
    ['BER LYR', 'Chocolate Flower', 'Berlanderia Lyrata', 'PER', 'EAS', 'FP', 'LO'],
    ['BAI MUL', 'Desert Marigold', 'Baileya Multiradiata', 'PER', 'EAS', 'FU', 'VL'],
    ['PEN EAT', 'Firecracker Penstemon', 'Penstemon Eatonii', 'PER', 'EAS', 'FP', 'LM'],
    ['CIR NEO', 'New Mexico Thistle', 'Cirsium Neomexicanum', 'PER', 'EAS', 'FP', 'LO'],
    ['PEN PAR', 'Parry\'s Penstemon', 'Penstemon Parryi', 'PER', 'EAS', 'FU', 'LO'],
    ['DIE SP', 'Tansy Aster', 'Dieteria Sp.', 'PER', 'EAS', 'FP', 'LO'],
    ['DAT WRI', 'Sacred Datura', 'Datura Wrightii', 'PER', 'EAS', 'FP', 'LO'],
    ['MAU ANT', 'Snapdragon Vine', 'Maurandella Antirrhiniflora', 'VIN', 'EAS', 'FP', 'LM']
]

# list of seed classifications
seed_types_list = [
    ['ANN', 'Annual'],
    ['GRA', 'Grass'],
    ['GRO', 'Groundcover'],
    ['PER', 'Perennial'],
    ['SHR', 'Shrub'],
    ['SUB', 'Subshrub'],
    ['TRE', 'Tree'],
    ['VIN', 'Vine']
]

seed_difficulty_list = [
    ['DIF', 'Difficult'],
    ['EAS', 'Easy'],
    ['MED', 'Medium'],
    ['UNK', 'Unknown']
]

# list of seed germination information
seed_sun_amt_list = [
    ['FU', 'Full'],
    ['FP', 'Full or Partial'],
    ['PA', 'Partial'],
    ['UNK', 'Unknown']
]

seed_water_amt_list = [
    ['HI', 'High'],
    ['MH', 'Moderate to High'],
    ['MO', 'Moderate'],
    ['LM', 'Low to Moderate'],
    ['LO', 'Low'],
    ['VL', 'Very Low'],
    ['UNK', 'Unknown']
]

# list of seed profile images
seed_profile_imgs_list = [
    ['COR TIN', "./seed_profile_imgs/cor_tin.jpg", "By Danielle Carlock"],
    ['PRO PAR', "./seed_profile_imgs/pro_par.jpeg", "By Frankiecoburn"],
    ['BOU CUR', "./seed_profile_imgs/bou_cur.jpg", "By Max Licher"],
    ['HIL RIG', "./seed_profile_imgs/hil_rig.jpg", "By Danielle Carlock"], 
    ['CON GRE', "./seed_profile_imgs/con_gre.jpg", "By Danielle Carlock"], 
    ['BAH PAR', "./seed_profile_imgs/bah_par.jpg", "By eric_hough"], 
    ['VAU CAL', "./seed_profile_imgs/vau_cal.jpg", "By pelser (iNaturalist)"], 
    ['ABU PAL', "./seed_profile_imgs/abu_pal.jpg", "By Sue Carnahan"],
    ['ENC FAR', "./seed_profile_imgs/enc_far.jpg", "By Danielle Carlock"], 
    ['DOD VIS', "./seed_profile_imgs/dod_vis.jpg", "By Danielle Carlock"],  
    ['CAL ERI', "./seed_profile_imgs/cal_eri.jpg", "By Danielle Carlock"], 
    ['ACO WRI', "./seed_profile_imgs/aco_wri.jpg", "By Danielle Carlock"], 
    ['ABU INC', "./seed_profile_imgs/abu_inc.jpg", "By Danielle Carlock"], 
    ['BEB JUN', "./seed_profile_imgs/beb_jun.jpg", "By tphender (iNaturalist)"], 
    ['SPH AMB', "./seed_profile_imgs/sph_amb.jpg", "By Danielle Carlock"], 
    ['GOS THU', "./seed_profile_imgs/gos_thu.jpg", "By Danielle Carlock"], 
    ['THY PEN', "./seed_profile_imgs/thy_pen.jpg", "By Anita Gould (flickr)"], 
    ['ERI DIV', "./seed_profile_imgs/eri_div.jpg", "By Danielle Carlock"], 
    ['SEN COV', "./seed_profile_imgs/sen_cov.jpg", "By Danielle Carlock"], 
    ['PRO VEL', "./seed_profile_imgs/pro_vel.jpg", "By ck2az (iNaturalist)"], 
    ['PAR FLO', "./seed_profile_imgs/par_flo.jpg", "By Danielle Carlock"], 
    ['STR ODO', "./seed_profile_imgs/str_odo.jpg", "By Patrick Alexander (Lady Bird Johnson Wildflower Center)"], 
    ['CHI LIN', "./seed_profile_imgs/chi_lin.jpg", "By Danielle Carlock"], 
    ['CHI LIN ARC', "./seed_profile_imgs/chi_lin_arc.jpg", "By Danielle Carlock"], 
    ['OLN TES', "./seed_profile_imgs/oln_tes.jpg", "By Danielle Carlock"], 
    ['PAR MIC', "./seed_profile_imgs/par_mic.jpeg", "By wonita (iNaturalist)"], 
    ['GAI SP', "./seed_profile_imgs/gai_sp.jpg", "By Danielle Carlock"], 
    ['BER LYR', "./seed_profile_imgs/ber_lyr.jpg", "By Danielle Carlock"], 
    ['BAI MUL', "./seed_profile_imgs/bai_mul.jpg", "By Danielle Carlock"], 
    ['PEN EAT', "./seed_profile_imgs/pen_eat.jpg", "By Steve Leavitt (iNaturalist)"], 
    ['CIR NEO', "./seed_profile_imgs/cir_neo.jpg", "By Danielle Carlock"], 
    ['PEN PAR', "./seed_profile_imgs/pen_par.jpg", "By Danielle Carlock"], 
    ['DIE SP', "./seed_profile_imgs/die_sp.jpg", "By ezpixels"], 
    ['DAT WRI', "./seed_profile_imgs/dat_wri.jpg", "By unknown"], 
    ['MAU ANT', "./seed_profile_imgs/mau_ant.jpg", "By Danielle Carlock"], 
]

# dataframe of seed profiles
seed_profiles_df = pd.DataFrame(seed_profiles_list, columns=['Seed ID', 'Common Name', 'Botanical Name', 'Type ID', 'Difficulty ID', 'Sun Amt ID', 'Water Amt ID'])

# dataframe of seed classifications
seed_types_df = pd.DataFrame(seed_types_list, columns=['Type ID', 'Type'])
seed_types_options = pd.DataFrame(seed_types_df['Type'])

seed_difficulty_df = pd.DataFrame(seed_difficulty_list, columns=['Difficulty ID', 'Difficulty'])
seed_difficulty_options = pd.DataFrame(seed_difficulty_df['Difficulty'])

# dataframe of seed germination information
seed_sun_amt_df = pd.DataFrame(seed_sun_amt_list, columns=['Sun Amt ID', 'SunAmt'])
seed_sun_amt_options = pd.DataFrame(seed_sun_amt_df['SunAmt'])

seed_water_amt_df = pd.DataFrame(seed_water_amt_list, columns=['Water Amt ID', 'WaterAmt'])
seed_water_amt_options = pd.DataFrame(seed_water_amt_df['WaterAmt'])

# dataframe of seed profile images
seed_profile_imgs_df = pd.DataFrame(seed_profile_imgs_list, columns=['Seed ID', 'Img', 'Author'])

# generate full seed profile dataframe

full_seed_profiles_df = pd.merge(
    pd.merge(
        pd.merge(
            pd.merge(
                pd.merge(seed_profiles_df, seed_profile_imgs_df, how='inner', on='Seed ID'),
                seed_water_amt_df, how='inner', on='Water Amt ID'), 
        seed_sun_amt_df, how='inner', on='Sun Amt ID'), 
    seed_difficulty_df, how='inner', on='Difficulty ID'), 
seed_types_df, how='inner', on='Type ID'
)

# function to filter seed profiles
def get_filtered_profiles(qry):
    df = full_seed_profiles_df

    if qry == "":
        results = df
    else:
        results = df.query(qry)

    return results

# CALCULATE NUMBER OF COLUMNS PER ROW
def create_seed_profile_columns(df, num_of_columns):
    num_of_profiles = len(df)

    num_of_rows = (num_of_profiles + num_of_columns - 1) // num_of_columns

    return num_of_rows