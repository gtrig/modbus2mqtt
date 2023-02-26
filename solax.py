# 0x0000GridVoltage(X1)RGridVoltage0.1VUint161
# 0x0001GridCurrent(X1)RGridCurrent0.1VInt161
# 0x0002GridPower(X1)RGridPower1WInt161
# 0x0003PvVoltage1(Hybrid)RPvVoltage10.1VUint161
# 0x0004PvVoltage2(Hybrid)RPvVoltage20.1VUint161
# 0x0005PvCurrent1(Hybrid)RPvCurrent10.1AUint161
# 0x0006PvCurrent2(Hybrid)RPvCurrent20.1AUint161
# 0x0007GridFrequency(X1)RGridFrequency0.01HzUint161
# 0x0008TemperatureRradiator temperature1℃int161
# 0x0009RunModeRRunMode—Uint161
# 0x000APowerdc1(Hybrid)RPowerdc11WUint161
# 0x000BPowerdc2(Hybrid)RPowerdc21WUint1610x000CTemperFaultValueRTemperFaultValue1℃int161
# 0x000DPv1VoltFaultValueRPv1VoltFaultValue0.1VUint161
# 0x000EPv2VoltFaultValueRPv2VoltFaultValue0.1VUint161
# 0x000FGfciFaultValueRGfciFaultValue1mAUint161
# 0x0010GridVoltFaultValueRGridVoltFaultValue0.1VUint161
# 0x0011GridFreqFaultValueTRGridFreqFaultValueT0.01HzUint161
# 0x0012DciFaultValueRDciFaultValue1mAUint161
# 0x0013TimeCountDownRTimeCountDown1msUint161
# 0x0014BatVoltage_Charge1RBatVoltage_Charge10.1VInt161
# 0x0015BatCurrent_Charge1RBatCurrent_Charge10.1Aint161
# 0x0016Batpower_Charge1RBatpower_Charge11Wint161
# 0x0017BMS_Connect_StateR0:Disconnected
# 1:Connected-Uint161
# 0x0018TemperatureBatRTemperatureBat1℃int161
# 0x0019REVRREV0x001AREVRREV0x001BREVRREV0x001CBattery CapacityRBattery capacity1%Uint161
# 0x001DOutputEnergy_Charge.LSBROutputEnergy_Charge0.1KWhUint161
# 0x001EOutputEnergy_Charge.MSBROutputEnergy_Charge0.1KWhUint161
# 0x001FBMS Warning LSBRBMS Warning code1Uint161
# Uint161
# 0x0020
# OutputEnergy_Charge_today R OutputEnergy_Charge_today 0.1KWh
# 0x0021InputEnergy_Charge.LSBRInputEnergy_Charge0.1KWhUint161
# 0x0022InputEnergy_Charge.MSBRInputEnergy_Charge0.1KWhUint161
# 0x0023InputEnergy_Charge_todayRInputEnergy_Charge_today 0.1KWhUint161
# 0x0024BMS ChargeMaxCurrentRBMS ChargeMaxCurrent
# (real time)0.1AUint161
# 0x0025BMS DischargeMaxCurrentRBMS DischargeMaxCurrent
# (real time)0.1AUint161
# 0x0026BMS Warning MSBRBMS Warning code1Uint161
# 0x0027-0x003EREVRREV0x003FREVRREV0x0040InvFaultMessage.LSBR Inverter fault message LSBUint161
# 0x0041InvFaultMessage.MSBR Inverter fault message MSBUint161
# 0x0042REV
# R
# REV
# -
# -
# 10x0043Mgr FaultMessageRMgr FaultMessage0x0044REVRREV-1
# 0x0045REVRREV-1
# power to the grid
# （Postive mean generate power;
# R
# Negative mean Consumed power）
# (0x46:LSB,0x47:MSB)1w0x0046feedin_power(meter)
# 0x0048feedin_energy_total(meter) R
# 0x004A
# Uint16
# 1
# Int322
# energy to the grid
# (0x48:LSB,0x49:MSB)0.01kwh Uint322
# consum_energy_total(meter) Renergy form the grid
# (0x4A:LSB,0x4B:MSB)0.01kwh Uint322
# 0x004CEPS_Volt(X1)REPS_Volt0.1VUint161
# 0x004DEPS_Current(X1)REPS_Current0.1AUint161
# 0x004EEPS_Power(X1)REPS power1VAUint161
# 0x004FEPS_Frequency(X1)REPS_Frequency0.01HzUint161
# 0x0050Etoday_togridRToday Energy
# (Inverter AC Port)0.1kwhUint161
# 0x0051RevRRev-Uint161
# 0.001kwh Uint322
# 0x0052~x0053Etotal_togridRTotal Energy
# (Inverter AC Port)
# (0x52:LSB,0x53:MSB)
# 0x0054Lock StateR0:locked 1:unlocked
# 0x0055
# ~0x0065REVRREV
# 0x0066BusVoltR0x0067wDcvFaultVal0x0068-Uint161
# BusVolt0.1VUint161
# RwDcvFaultVal0.1VUint161
# wOverLoadFaultvalRwOverLoadFaultvalWUint161
# 0x0069wBatteryVoltFaultValRwBatteryVoltFaultVal0.1VUint161
# 0x006AGridVoltage_R(X3)RGridVoltage_R0.1VUint161
# 0x006BGridCurrent_R(X3)RGridCurrent_R0.1AInt161
# 0x006CGridPower_R(X3)RGridPower_R1WInt161
# 0x006DGridFrequency_R(X3)RGridFrequency_R0.01HzUint161
# 0x006EGridVoltage_S(X3)RGridVoltage_S0.1VUint161
# 0x006FGridCurrent_S(X3)RGridCurrent_S0.1AInt161
# 0x0070GridPower_S(X3)RGridPower_S1WInt161
# 0x0071GridFrequency_S(X3)RGridFrequency_S0.01HzUint161
# 0x0072GridVoltage_T(X3)RGridVoltage_T0.1VUint1610x0073GridCurrent_T(X3)RGridCurrent_T0.1AInt161
# 0x0074GridPower_T(X3)RGridPower_T1WInt161
# 0x0075GridFrequency_T(X3)RGridFrequency_T0.01HzUint161
# 0x0076EPS_Volt_R(X3)REPS_Volt_R0.1VUint161
# 0x0077EPS_Current_R(X3)REPS_Current_R0.1AUint161
# 0x0078EpsPowerActive_R(X3)REpsPowerActive_R1WUint161
# 0x0079EpsPowerS_R(X3)REpsPowerS_R1VAUint161
# 0x007AEPS_Volt_S(X3)REPS_Volt_S0.1VUint161
# 0x007BEPS_Current_S(X3)REPS_Current_S0.1AUint161
# 0x007CEpsPowerActive_S(X3)REpsPowerActive_S1WUint161
# 0x007DEpsPowerS_S(X3)REpsPowerS_S1VAUint161
# 0x007EEPS_Volt_T(X3)REPS_Volt_T0.1VUint161
# 0x007FEPS_Current_T(X3)REPS_Current_T0.1AUint161
# 0x0080EpsPowerActive_T(X3)REpsPowerActive_T1WUint161
# 0x0081EpsPowerS_T(X3)REpsPowerS_T1VAUint161
# RFeedinPower_Rphase
# (meter)
# (082:LSB,0x83:MSB)1WInt322
# RFeedinPower_Sphase
# (meter)
# (0x84:LSB,0x85:MSB)1WInt322
# 1WInt322
# 0x0082
# ~0x0083
# 0x0084
# ~0x0085
# FeedinPower_Rphase(X3)
# FeedinPower_Sphase(X3)
# 0x0086
# ~0x0087FeedinPower_Tphase(X3)RFeedinPower_Tphase
# (meter)
# (0x86:LSB,0x87:MSB)0x0088
# ~0x0089GridModeRunTime(X3)RGridModeRunTime
# (0x88:LSB,0x89:MSB)0.1HInt322
# 0x008A
# ~0x008BEpsModeRunTime(X3)REpsModeRunTime
# (0x8A:LSB,0x8B:MSB)0.1HInt322
# 0x008C
# ~0x008DNoramlRunTime(X1)RNoramlRunTime
# (0x8C:LSB,0x8D:MSB)0.1HInt322
# 0x008E
# ~0x008FEpsYieldTotalREpsYieldTotal
# (0x8E:LSB,0x8F:MSB)0.1KWhUint322
# 0x0090EpsYieldTodayREpsYieldToday0.1KWhUint161
# 0x0091EchargeTodayREchargeToday
# (Inverter AC Port)1KWhUint161REchargeTotal
# (Inverter AC Port)
# (0x92:LSB,0x93:MSB)1KWhUint322
# SolarEnergyTotalRSolarEnergyTotal
# (0x94:LSB,0x95:MSB)0.1KWhUint322
# 0x0096SolarEnergyTodayRSolarEnergyToday0.1KWhUint161
# 0x0097revRrevRenergy to the grid
# (meter)
# (0x98:LSB,0x99:MSB)0.01kwh Uint162
# energy form the
# grid(meter)
# (0x9A:LSB,0x9B:MSB)0.01kwh Uint162
# 0x0092
# ~0x0093EchargeTotal
# 0x0094
# ~0x0095
# 0x0098
# ~0x0099
# feedin_energy_today
# 0x009A
# ~0x009Bconsum_energy_todayR0x009C
# ~0x009DwActivePower
# (0x9C:LSB,0x9D:MSB)R1WInt322
# 0x009E
# ~0x009FwReactivePower
# (0x9E:LSB,0x9F:MSB)R1VarInt322
# 0x00A0
# ~0x00A1wActivePower_Upper
# (0xA0:LSB,0xA1:MSB)R1WInt322
# 0x00A2
# ~0x00A3wActivePower_Lower
# (0xA2:LSB,0xA3:MSB)R1WInt322
# 0x00A4
# ~0x00A5wReactivePowe_Upper
# (0xA4:LSB,0xA5:MSB)R1VarInt322
# 0x00A6
# ~0x00A7wReactivePower_Lower
# (0xA6:LSB,0xA7:MSB)R1VarInt322
# 0x00A8
# ~0x00A9feedin_power_Meter2Rpower to the grid
# (0xA8:LSB,0xA9:MSB)1wInt322
# 0x00AA
# ~0x00ABfeedin_energy_total_Meter2 Renergy to the grid
# (0xAA:LSB,0xAB:MSB)0.01kwh Uint322
# 0x00AC
# ~0x00ADconsum_energy_total_Meter2 Renergy form the grid
# (0xAC:LSB,0xAD:MSB)0.01kwh Uint322
# 0x00AE
# ~0x00AFfeedin_energy_today_Meter2 Renergy to the grid
# (0xAE:LSB,0xAF:MSB)0.01kwh Uint162
# 0x00B0
# ~0x00B1consum_energy_today_Meter2 Renergy form the grid
# (0xB0:LSB,0xB1:MSB)0.01kwh Uint162
# 0x00B2
# ~0x00B3FeedinPower_Rphase_Meter2 RFeedinPower_Rphase(X3)
# (0xB2:LSB,0xB3:MSB)
# Modbus power control
# (Positive mean
# charge;Negative mean
# discharge)
# 1W
# Int32
# 20x00B4
# ~0x00B5FeedinPower_Sphase_Meter2 RFeedinPower_Sphase(X3)
# (0xB4:LSB,0xB5:MSB)1WInt322
# 0x00B6
# ~0x00B7FeedinPower_Tphase_Meter2 RFeedinPower_Tphase(X3)
# (0xB6:LSB,0xB7:MSB)1WInt322
# 0x00B8Meter1CommunicationSateR0:Com Error 1:Normal1Uint161
# 0x00B9Meter2CommunicationSateR0:Com Error 1:Normal1Uint161
HoldingRegistersMap = [
    {
        "address": "0x0085",
        "length": 1,
        "name": "RTC-Seconds",
        "unit": "s",
        "type": "uint16",
        "scale": 1,
        "description": "RTC-Seconds",
    },
    {
        "address": "0x0086",
        "length": 1,
        "name": "RTC-Minutes",
        "unit": "m",
        "type": "uint16",
        "scale": 1,
        "description": "RTC-Minutes",
    },
    {
        "address": "0x0087",
        "length": 1,
        "name": "RTC-Hours",
        "unit": "h",
        "type": "uint16",
        "scale": 1,
        "description": "RTC-Hours",
    },
    {
        "address": "0x0088",
        "length": 1,
        "name": "RTC-Day",
        "unit": "d",
        "type": "uint16",
        "scale": 1,
        "description": "RTC-Day",
    },
    {
        "address": "0x0089",
        "length": 1,
        "name": "RTC-Months",
        "unit": "m",
        "type": "uint16",
        "scale": 1,
        "description": "RTC-Months",
    },
    {
        "address": "0x008A",
        "length": 1,
        "name": "RTC-Years",
        "unit": "y",
        "type": "uint16",
        "scale": 1,
        "description": "RTC-Years",
    },
]

InputRegistersMap = [
    {
        "address": "0x0000",
        "length": 1,
        "name": "Grid Voltage",
        "unit": "V",
        "type": "uint16",
        "scale": 0.1,
        "description": "Grif Voltage",

    },
    {
        "address": "0x0001",
        "length": 1,
        "name": "Grid Current",
        "unit": "A",
        "type": "int16",
        "scale": 0.1,
        "description": "Grid Current",
    },
    {
        "address": "0x0002",
        "length": 1,
        "name": "Grid Power",
        "unit": "W",
        "type": "int16",
        "scale": 1,
        "description": "Grid Power",
    },
    {
        "address": "0x0003",
        "length": 1,
        "name": "PV Voltage1",
        "unit": "V",
        "type": "uint16",
        "scale": 0.1,
        "description": "PV Voltage1",
    },
    {
        "address": "0x0004",
        "length": 1,
        "name": "PV Voltage2",
        "unit": "V",
        "type": "uint16",
        "scale": 0.1,
        "description": "PV Voltage2",
    },
    {
        "address": "0x0005",
        "length": 1,
        "name": "PV Current1",
        "unit": "A",
        "type": "uint16",
        "scale": 0.1,
        "description": "PV Current1",
    },
    {
        "address": "0x0006",
        "length": 1,
        "name": "PV Current2",
        "unit": "A",
        "type": "uint16",
        "scale": 0.1,
        "description": "PV Current2",
    },
    {
        "address": "0x0007",
        "length": 1,
        "name": "Grid Frequency",
        "unit": "Hz",
        "type": "uint16",
        "scale": 0.01,
        
        "description": "Grid Frequency",
    },
    {
        "address": "0x0008",
        "length": 1,
        "name": "Temperature",
        "unit": "C",
        "type": "int16",
        "scale": 1,   
        "description": "Temperature",
    },
    {
        "address": "0x000A",
        "length": 1,
        "name": "Powerdc1",
        "unit": "W",
        "type": "uint16",
        "scale": 1,
        "description": "Powerdc1",
    },
    {
        "address": "0x000B",
        "length": 1,
        "name": "Powerdc2",
        "unit": "W",
        "type": "uint16",
        "scale": 1,
        "description": "Powerdc2",
    },
    {
        "address": "0x0014",
        "length": 1,
        "name": "BatVoltage_Charge1",
        "unit": "V",
        "type": "int16",
        "scale": 0.1,
        "description": "BatVoltage_Charge1",
    },
    {
        "address": "0x0015",
        "length": 1,
        "name": "BatCurrent_Charge1",
        "unit": "A",
        "type": "int16",
        "scale": 0.1,
        "description": "BatCurrent_Charge1",
    },
    {
        "address": "0x0016",
        "length": 1,   
        "name": "Batpower_Charge1",
        "unit": "W",
        "type": "int16",
        "scale": 1,
        "description": "Batpower_Charge1",
    },
    {
        "address": "0x0018",
        "length": 1,
        "name": "TemperatureBat",
        "unit": "C",
        "type": "int16",
        "scale": 1,
        "description": "TemperatureBat",
    },
    {
        "address": "0x001C",
        "length": 1,
        "name": "Battery Capacity",
        "unit": "%",
        "type": "uint16",
        "scale": 1,
        "description": "Battery SOC",
    },
    {
        "address": "0x001D",
        "length": 2,
        "name": "OutputEnergy_Charge",
        "unit": "KWh",
        "type": "uint32",
        "scale": 0.1,
        "description": "OutputEnergy_Charge",
    },
    {
        "address": "0x0020",
        "length": 1,
        "name": "OutputEnergy_Charge_today",
        "unit": "KWh",
        "type": "uint16",
        "scale": 0.1,
        "description": "OutputEnergy_Charge_today",
    },
    {
        "address": "0x0021",
        "length": 2,
        "name": "InputEnergy_Charge",
        "unit": "KWh",
        "type": "uint32",
        "scale": 0.1,
        "description": "InputEnergy_Charge",
    },
    {
        "address": "0x0023",
        "length": 1,
        "name": "InputEnergy_Charge_today",
        "unit": "KWh",
        "type": "uint16",
        "scale": 0.1,
        "description": "InputEnergy_Charge.today",
    },
    {
        "address": "0x0024",
        "length": 1,
        "name": "BMS ChargeMaxCurrent",
        "unit": "A",
        "type": "uint16",
        "scale": 0.1,
        "description": "BMS ChargeMaxCurrent",
    },
    {
        "address": "0x0025",
        "length": 1,
        "name": "BMS DischargeMaxCurrent",
        "unit": "A",
        "type": "uint16",
        "scale": 0.1,
        "description": "BMS DischargeMaxCurrent",
    },
    {
        "address": "0x0046",
        "length": 2,
        "name": "feedin_power(meter)",
        "unit": "W",
        "type": "int32",
        "scale": 1,
        "description": "power to the grid (Postive mean generate power; Negative mean Consumed power) (0x46:LSB,0x47:MSB)",
    },
    {
        "address": "0x0048",
        "length": 2,
        "name": "feedin_energy_total(meter)",
        "unit": "KWh",
        "type": "uint32",
        "scale": 0.01,
        "description": "Total energy to the grid (0x48:LSB,0x49:MSB)",
    },
    {
        "address": "0x004A",
        "length": 2,
        "name": "consum_energy_total(meter)",
        "unit": "KWh",
        "type": "uint32",
        "scale": 0.01,
        "description": "Total energy to the grid (0x4A:LSB,0x4B:MSB)",
    },
    {
        "address": "0x004C",
        "length": 1,
        "name": "EPS_Volt",
        "unit": "V",
        "type": "uint16",
        "scale": 0.1,
        "description": "EPS_Volt",
    },
    {
        "address": "0x004D",
        "length": 1,
        "name": "EPS_Current",
        "unit": "A",
        "type": "uint16",
        "scale": 0.1,
        "description": "EPS_Current",
    },
    {
        "address": "0x004E",
        "length": 1,
        "name": "EPS_Power",
        "unit": "VA",
        "type": "uint16",
        "scale": 1,
        "description": "EPS_Power",
    },
    {
        "address": "0x004F",
        "length": 1,
        "name": "EPS_Frequency",
        "unit": "Hz",
        "type": "uint16",
        "scale": 0.01,
        "description": "EPS_Frequency",
    },
    {
        "address": "0x0050",
        "length": 1,
        "name": "Etoday_togrid",
        "unit": "KWh",
        "type": "uint16",
        "scale": 0.1,
        "description": "Etoday_togrid",
    },
    {
        "address": "0x0052",
        "length": 2,
        "name": "Etotal_togrid",
        "unit": "KWh",
        "type": "uint32",
        "scale": 0.001,
        "description": "Etotal_togrid",
    },
    {
        "address": "0x0054",
        "length": 1,
        "name": "Locked",
        "unit": "",
        "type": "uint16",
        "scale": 1,
        "description": "Locked",
    },
    {
        "address": "0x0092",
        "length": 2,
        "name": "EchargeTotal",
        "unit": "KWh",
        "type": "uint32",
        "scale": 1,
        "description": "EchargeTotal",
    },
    {
        "address": "0x0094",
        "length": 2,
        "name": "SolarEnergyTotal",
        "unit": "KWh",
        "type": "uint32",
        "scale": 0.1,
        "description": "SolarEnergyTotal",
    },
    {
        "address": "0x0096",
        "length": 1,
        "name": "SolarEnergyToday",
        "unit": "KWh",
        "type": "uint16",
        "scale": 0.1,
        "description": "SolarEnergyToday",
    },
    {
        "address": "0x0098",
        "length": 2,
        "name": "feedin_energy_today",
        "unit": "KWh",
        "type": "uint32",
        "scale": 0.01,
        "description": "feedin_energy_today",
    },
    {
        "address": "0x009A",
        "length": 2,
        "name": "consum_energy_today",
        "unit": "KWh",
        "type": "uint32",
        "scale": 0.01,
        "description": "consum_energy_today",
    },
    {
        "address": "0x009C",
        "length": 2,
        "name": "wActivePower",
        "unit": "W",
        "type": "int32",
        "scale": 1,
        "description": "wActivePower",
    },
    {
        "address": "0x009E",
        "length": 2,
        "name": "wReactivePower",
        "unit": "VAR",
        "type": "int32",
        "scale": 1,
        "description": "wReactivePower",
    },
    {
        "address": "0x00A0",
        "length": 2,
        "name": "wActivePower_Upper",
        "unit": "W",
        "type": "int32",
        "scale": 1,
        "description": "wActivePower_Upper",
    },
    {
        "address": "0x00A2",
        "length": 2,
        "name": "wActivePower_Lower",
        "unit": "W",
        "type": "int32",
        "scale": 1,
        "description": "wActivePower_Lower",
    },
    {
        "address": "0x00A4",
        "length": 2,
        "name": "wReactivePower_Upper",
        "unit": "VAR",
        "type": "int32",
        "scale": 1,
        "description": "wReactivePower_Upper",
    },
    {
        "address": "0x00A6",
        "length": 2,
        "name": "wReactivePower_Lower",
        "unit": "VAR",
        "type": "int32",
        "scale": 1,
        "description": "wReactivePower_Lower",
    },
    {
        "address": "0x00A8",
        "length": 2,
        "name": "feedin_power_Meter2",
        "unit": "W",
        "type": "uint32",
        "scale": 1,
        "description": "feedin_power_Meter2",
    },
    {
        "address": "0x00AA",
        "length": 2,
        "name": "feedin_energy_total_Meter2",
        "unit": "KWh",
        "type": "uint32",
        "scale": 0.01,
        "description": "feedin_energy_total_Meter2",
    },
    {
        "address": "0x00AC",
        "length": 2,
        "name": "consum_energy_total_Meter2",
        "unit": "KWh",
        "type": "uint32",
        "scale": 0.01,
        "description": "consum_energy_total_Meter2",
    },
    {
        "address": "0x00AE",
        "length": 2,
        "name": "feedin_energy_today_Meter2",
        "unit": "KWh",
        "type": "uint32",
        "scale": 0.01,
        "description": "feedin_energy_today_Meter2",
    },
    {
        "address": "0x00B0",
        "length": 2,
        "name": "consum_energy_today_Meter2",
        "unit": "KWh",
        "type": "uint32",
        "scale": 0.01,
        "description": "consum_energy_today_Meter2",
    },
    {
        "address": "0x00BA",
        "length": 1,
        "name": "GridVoltage",
        "unit": "V",
        "type": "uint16",
        "scale": 0.1,
        "description": "GridVoltage",
    },
    {
        "address": "0x00BB",
        "length": 1,
        "name": "GridCurrent",
        "unit": "A",
        "type": "int16",
        "scale": 0.1,
        "description": "GridCurrent",
    },
    {
        "address": "0x00BC",
        "length": 1,
        "name": "GridPower",
        "unit": "W",
        "type": "int16",
        "scale": 1,
        "description": "GridPower",
    },
    {
        "address": "0x00BD",
        "length": 1,
        "name": "GridFrequency",
        "unit": "Hz",
        "type": "uint16",
        "scale": 0.01,
        "description": "GridFrequency",
    },
    {
        "address": "0x00BE",
        "length": 1,
        "name": "Temperature2",
        "unit": "°C",
        "type": "int16",
        "scale": 0.1,
        "description": "Temperature2",
    },
    {
        "address": "0x00C0",
        "length": 2,
        "name": "feedin_power",
        "unit": "W",
        "type": "int32",
        "scale": 1,
        "description": "feedin_power2",
    },
]

proccessingMap = [
    {
        "name": "PV Power1",
        "type": "mul",
        "registers": ["PV Voltage1", "PV Current1"],
    },
    {
        "name": "PV Power2",
        "type": "mul",
        "registers": ["PV Voltage2", "PV Current2"],
    },
    {
        "name": "TotalSolarPower",
        "type": "sum",
        "registers": ["PV Power1", "PV Power2"],
    },
]

testRegisterMap = [
    {
        "address": "0x0014",
        "length": 1,
        "name": "BatVoltage_Charge1",
        "unit": "V",
        "type": "int16",
        "scale": 0.1,
        "description": "BatVoltage_Charge1",
    },
    {
        "address": "0x0015",
        "length": 1,
        "name": "BatCurrent_Charge1",
        "unit": "A",
        "type": "int16",
        "scale": 0.1,
        "description": "BatCurrent_Charge1",
    },
    {
        "address": "0x0016",
        "length": 1,   
        "name": "Batpower_Charge1",
        "unit": "W",
        "type": "int16",
        "scale": 1,
        "description": "Batpower_Charge1",
    },
    {
        "address": "0x0018",
        "length": 1,
        "name": "TemperatureBat",
        "unit": "C",
        "type": "int16",
        "scale": 1,
        "description": "TemperatureBat",
    },
    {
        "address": "0x001C",
        "length": 1,
        "name": "Battery Capacity",
        "unit": "%",
        "type": "uint16",
        "scale": 1,
        "description": "Battery SOC",
    },

]

