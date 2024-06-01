import os
import pandas as pd
from tabulate import tabulate
from tqdm import tqdm

def find_address_info(search_file, target_file_merkly, target_file_holograph, target_file_altitude, target_file_dappgate, target_file_level_bridge, target_file_l2telegraph, target_file_omnibase, target_file_omnihub, target_file_omnisea, target_file_whale, target_file_nomis, target_file_dexalot, target_file_dfk, target_file_harmony, target_file_l2marathon, target_file_mavia, target_file_orderly, target_file_superform, target_file_angle_protocol, target_file_canto, target_file_ethena, target_file_frax, target_file_gaszip, target_file_kresko, target_file_maverick, target_file_metastreet, target_file_omni_x, target_file_polyhedra, target_file_shimmer, target_file_swell, target_file_telos, target_file_tenet, target_file_tevaera, target_file_venus, target_file_woofi, output_file, show_zero_eligible=False):
    def load_file(file_path):
        with open(file_path, 'r') as file:
            return file.readlines()
    
    def process_line_to_dict(lines, key_index=0, value_index=None, delimiter=','):
        data = {}
        for line in lines:
            parts = line.strip().lower().split(delimiter)
            key = parts[key_index]
            value = parts[value_index] if value_index is not None else "Eligible"
            data[key] = value
        return data
    

    filename = "result"
    if os.path.exists(filename):
        pass
    else:
        os.mkdir("result")
    target_lines_merkly = load_file(target_file_merkly)
    target_lines_holograph = load_file(target_file_holograph)
    target_lines_altitude = load_file(target_file_altitude)
    target_lines_dappgate = load_file(target_file_dappgate)
    target_lines_level_bridge = load_file(target_file_level_bridge)
    target_lines_l2telegraph = load_file(target_file_l2telegraph)
    target_lines_omnibase = load_file(target_file_omnibase)
    target_lines_omnihub = load_file(target_file_omnihub)
    target_lines_omnisea = load_file(target_file_omnisea)
    target_lines_whale = load_file(target_file_whale)
    target_lines_nomis = load_file(target_file_nomis)
    target_lines_dexalot = load_file(target_file_dexalot)
    target_lines_dfk = load_file(target_file_dfk)
    target_lines_harmony = load_file(target_file_harmony)
    target_lines_l2marathon = load_file(target_file_l2marathon)
    target_lines_mavia = load_file(target_file_mavia)
    target_lines_orderly = load_file(target_file_orderly)
    target_lines_superform = load_file(target_file_superform)
    target_lines_angle_protocol = load_file(target_file_angle_protocol)
    target_lines_canto = load_file(target_file_canto)
    target_lines_ethena = load_file(target_file_ethena)
    target_lines_frax = load_file(target_file_frax)
    target_lines_gaszip = load_file(target_file_gaszip)
    target_lines_kresko = load_file(target_file_kresko)
    target_lines_maverick = load_file(target_file_maverick)
    target_lines_metastreet= load_file(target_file_metastreet)
    target_lines_omni_x = load_file(target_file_omni_x)
    target_lines_polyhedra = load_file(target_file_polyhedra)
    target_lines_shimmer = load_file(target_file_shimmer)
    target_lines_swell = load_file(target_file_swell)
    target_lines_telos = load_file(target_file_telos)
    target_lines_tenet = load_file(target_file_tenet)
    target_lines_tevaera = load_file(target_file_tevaera)
    target_lines_venus = load_file(target_file_venus)
    target_lines_woofi = load_file(target_file_woofi)

    merkly_points = process_line_to_dict(target_lines_merkly, key_index=0, value_index=1)
    l2telegraph_tier = process_line_to_dict(target_lines_l2telegraph, key_index=0, value_index=1)
    holograph_percentages = process_line_to_dict(target_lines_holograph, key_index=0, value_index=4)
    altitude_percentages = process_line_to_dict(target_lines_altitude, key_index=0, value_index=1)
    omnibase_coefficient = process_line_to_dict(target_lines_omnibase, key_index=0, value_index=1)
    omnihub_percentages = process_line_to_dict(target_lines_omnihub, key_index=0, value_index=1)
    whale_txs = process_line_to_dict(target_lines_whale, key_index=0, value_index=1)
    nomis_percentages = process_line_to_dict(target_lines_nomis, key_index=0, value_index=3)
    dappgate_data = process_line_to_dict(target_lines_dappgate, key_index=0)
    level_bridge_data = process_line_to_dict(target_lines_level_bridge, key_index=0)
    omnisea_data = process_line_to_dict(target_lines_omnisea, key_index=0)
    dexalot_data = process_line_to_dict(target_lines_dexalot, key_index=0)
    dfk_percentages = process_line_to_dict(target_lines_dfk, key_index=0, value_index=3)
    harmony_data = process_line_to_dict(target_lines_harmony, key_index=0)
    l2marathon_transfers_count = process_line_to_dict(target_lines_l2marathon, key_index=0, value_index=1)
    mavia_data = process_line_to_dict(target_lines_mavia, key_index=0)
    orderly_percentages = process_line_to_dict(target_lines_orderly, key_index=0, value_index=1)
    superform_percentages = process_line_to_dict(target_lines_superform, key_index=0, value_index=1)
    angle_protocol_percentages = process_line_to_dict(target_lines_angle_protocol, key_index=0, value_index=2)
    canto_percentages = process_line_to_dict(target_lines_canto, key_index=0, value_index=1)
    ethena_percentages = process_line_to_dict(target_lines_ethena, key_index=0, value_index=4)
    frax_percentages = process_line_to_dict(target_lines_frax, key_index=0, value_index=2)
    gaszip_points = process_line_to_dict(target_lines_gaszip, key_index=0, value_index=1)
    kresko_data = process_line_to_dict(target_lines_kresko, key_index=0)
    maverick_percentages = process_line_to_dict(target_lines_maverick, key_index=1, value_index=2)
    omni_x_percentages = process_line_to_dict(target_lines_omni_x, key_index=0, value_index=1)
    polyhedra_percentages = process_line_to_dict(target_lines_polyhedra, key_index=0, value_index=1)
    shimmer_percentages = process_line_to_dict(target_lines_shimmer, key_index=0, value_index=3)
    swell_percentages = process_line_to_dict(target_lines_swell, key_index=0, value_index=1)
    telos_data = process_line_to_dict(target_lines_telos, key_index=0)
    tenet_percentages = process_line_to_dict(target_lines_tenet, key_index=0, value_index=1)
    tevaera_percentages = process_line_to_dict(target_lines_tevaera, key_index=0, value_index=1)
    venus_data = process_line_to_dict(target_lines_venus, key_index=0)
    woofi_percentages = process_line_to_dict(target_lines_woofi, key_index=0, value_index=1)
    metastreet_percentages = process_line_to_dict(target_lines_metastreet, key_index=0, value_index=1)
    
    results = []
    
    with open(search_file, 'r') as search:
        total_lines = len(search.readlines())
        search.seek(0)
        with tqdm(total=total_lines, desc="Processing Addresses", unit="address") as pbar:
            for search_string in search:
                search_string = search_string.strip().lower()
                
                merkly_point = merkly_points.get(search_string, '0')
                holograph_percentage = holograph_percentages.get(search_string, '0')
                altitude_percentage = altitude_percentages.get(search_string, '0')
                dappgate_value = dappgate_data.get(search_string, 'Not Eligible')
                level_bridge_value = level_bridge_data.get(search_string, 'Not Eligible')
                omnibase_value = omnibase_coefficient.get(search_string, '0')
                omnihub_percentage = omnihub_percentages.get(search_string, '0')
                omnisea_value = omnisea_data.get(search_string, 'Not Eligible')
                whale_tx = whale_txs.get(search_string, '0')
                nomis_percentage = nomis_percentages.get(search_string, '0')
                l2telegraph_tier_value = l2telegraph_tier.get(search_string, '0')
                dexalot_value = dexalot_data.get(search_string, 'Not Eligible')
                dfk_percentage = dfk_percentages.get(search_string, '0')
                harmony_value = harmony_data.get(search_string, 'Not Eligible')
                l2marathon_transfer_count = l2marathon_transfers_count.get(search_string, '0')
                mavia_value = mavia_data.get(search_string, 'Not Eligible')
                orderly_percentage = orderly_percentages.get(search_string, '0')
                superform_percentage = superform_percentages.get(search_string, '0')
                angle_protocol_percentage = angle_protocol_percentages.get(search_string, '0')
                canto_percentage = canto_percentages.get(search_string, '0')
                ethena_percentage = ethena_percentages.get(search_string, '0')
                frax_percentage = frax_percentages.get(search_string, '0')
                gaszip_point = gaszip_points.get(search_string, '0')
                kresko_value = kresko_data.get(search_string, 'Not Eligible')
                maverick_percentage = maverick_percentages.get(search_string, '0')
                omni_x_percentage = omni_x_percentages.get(search_string, '0')
                polyhedra_percentage = polyhedra_percentages.get(search_string, '0')
                shimmer_percentage = shimmer_percentages.get(search_string, '0')
                swell_percentage = swell_percentages.get(search_string, '0')
                telos_value = telos_data.get(search_string, 'Not Eligible')
                tenet_percentage = tenet_percentages.get(search_string, '0')
                tevaera_percentage = tevaera_percentages.get(search_string, '0')
                venus_value = venus_data.get(search_string, 'Not Eligible')
                woofi_percentage = woofi_percentages.get(search_string, '0')
                metastreet_percentage = metastreet_percentages.get(search_string, '0')
                
                if show_zero_eligible or any([
                    merkly_point != '0', 
                    holograph_percentage != '0', 
                    altitude_percentage != '0', 
                    dappgate_value != 'Not Eligible', 
                    level_bridge_value != 'Not Eligible', 
                    omnibase_value != '0', 
                    omnihub_percentage != '0', 
                    omnisea_value != 'Not Eligible', 
                    whale_tx != '0', 
                    nomis_percentage != '0',
                    l2telegraph_tier_value != '0',
                    dexalot_value != 'Not Eligible',
                    dfk_percentage != '0',
                    harmony_value != 'Not Eligible',
                    l2marathon_transfer_count != '0',
                    mavia_value != 'Not Eligible',
                    orderly_percentage != '0',
                    superform_percentage != '0',
                    angle_protocol_percentage != '0',
                    canto_percentage != '0',
                    ethena_percentage != '0',
                    frax_percentage != '0',
                    gaszip_point != '0',
                    kresko_value != 'Not Eligible',
                    maverick_percentage != '0',
                    omni_x_percentage != '0',
                    polyhedra_percentage != '0',
                    shimmer_percentage != '0',
                    swell_percentage != '0',
                    telos_value != 'Not Eligible',
                    tenet_percentage != '0',
                    tevaera_percentage != '0',
                    venus_value != 'Not Eligible',
                    woofi_percentage != '0',
                    metastreet_percentage != '0'
                ]):
                    results.append([
                        search_string,
                        merkly_point,
                        holograph_percentage,
                        altitude_percentage,
                        dappgate_value,
                        level_bridge_value,
                        omnibase_value,
                        omnihub_percentage,
                        omnisea_value,
                        whale_tx,
                        nomis_percentage,
                        l2telegraph_tier_value,
                        dexalot_value,
                        dfk_percentage,
                        harmony_value,
                        l2marathon_transfer_count,
                        mavia_value,
                        orderly_percentage,
                        superform_percentage,
                        angle_protocol_percentage,
                        canto_percentage,
                        ethena_percentage,
                        frax_percentage,
                        gaszip_point,
                        kresko_value,
                        maverick_percentage,
                        omni_x_percentage,
                        polyhedra_percentage,
                        shimmer_percentage,
                        swell_percentage,
                        telos_value,
                        tenet_percentage,
                        tevaera_percentage,
                        venus_value,
                        woofi_percentage,
                        metastreet_percentage
                    ])
                pbar.update(1)
                
    df = pd.DataFrame(results, columns=[
        'Address', 'Merkly Points', 'Percent Holograph', 'Percent Altitude', 'Dappgate', 'Level Bridge', 
        'Coefficient Omnibase', 'Percent Omnihub', 'Omnisea', 'TXS Whale', 'Percent Nomis', 'L2telegraph',
        'Dexalot', 'Percent DFK', 'Harmony', 'TXS L2marathon', 'Mavia', 'Percent Orderly', 'Percent Superform',
        'Percent Angle Protocol', 'Percent Canto', 'Percent Ethena', 'Percent Frax', 'Points Gaszip', 'Kresko',
        'Percent Maverick', 'Percent Omni X', 'Percent Polyhedra', 'Percent Shimmer', 'Percent Swell', 'Telos',
        'Percent Tenet', 'Percent Tevaera', 'Venus', 'Percent Woofi', 'Percent Metastreet'    
    ])
    
    with open(output_file, 'w') as output:
        output.write(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))
        
    print('Успешно! TG Channel: @crypto_armored. Результат сохранен в result/result.txt')

show_zero_eligible = input("Отобразить адреса, которые не элигибл ни к одному из дропов? (Yes/No): ").strip().lower() == 'yes'

find_address_info(
    'user_data/evm.txt', 'checkers/merkly.txt', 'checkers/holograph.txt', 'checkers/altitude.txt', 'checkers/dappgate.txt', 'checkers/lvl-bridge.txt',
    'checkers/l2telegraph.txt', 'checkers/omnibase.txt', 'checkers/omnihub.txt', 'checkers/omnisea.txt', 'checkers/whale.txt', 'checkers/nomis.txt', 
    'checkers/dexalot.txt', 'checkers/dfk.txt', 'checkers/harmony.txt', 'checkers/l2marathon.txt', 'checkers/mavia.txt', 'checkers/orderly.txt', 'checkers/superform.txt',
    'checkers/angle_protocol.txt', 'checkers/canto.txt', 'checkers/ethena.txt', 'checkers/frax.txt', 'checkers/gaszip.txt', 'checkers/kresko.txt', 'checkers/maverick.txt',
    'checkers/metastreet.txt', 'checkers/omni_x.txt', 'checkers/polyhedra.txt', 'checkers/shimmer.txt', 'checkers/swell.txt', 'checkers/telos.txt', 'checkers/tenet.txt',
    'checkers/tevaera.txt', 'checkers/venus.txt', 'checkers/woofi.txt', 'result/result.txt', show_zero_eligible
)
