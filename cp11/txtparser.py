import sys

def main():
    bounds = [  0, 4, 14, 25, 31, 37, 41, 42, 43,
                44, 49, 51, 60, 62, 64, 68, 69, 71,
                73, 75, 77, 79, 83, 84, 86, 88, 90,
                96, 102, 107, 108, 109, 114, 115, 120,
                121, 126, 127, 147, 148, 154, 160, 161,
                166, 170, 174, 176, 179, 180, 184, 190,
                194, 196, 197
              ]
    # create column labels
    columns = [
    "HR", "Name", "DM", "HD", "SAO", "FK5", "IRflag", "r_IRflag", "Multiple", "ADS", 
    "ADScomp", "VarID", "RAh1900", "RAm1900", "RAs1900", "DE-1900", "DEd1900", 
    "DEm1900", "DEs1900", "RAh", "RAm", "RAs", "DE-", "DEd", "DEm", "DEs", "GLON", 
    "GLAT", "Vmag", "n_Vmag", "u_Vmag", "B-V", "u_B-V", "U-B", "u_U-B", "R-I", 
    "n_R-I", "SpType", "n_SpType", "pmRA", "pmDE", "n_Parallax", "Parallax", 
    "RadVel", "n_RadVel", "l_RotVel", "RotVel", "u_RotVel", "Dmag", "Sep", 
    "MultID", "MultCnt", "NoteFlag"
    ]
    for line in sys.stdin:
        # remove EOL character
        line = line.rstrip('\n')
        line = line.replace(",", " ")
        s = ''
        for i in range(0, len(bounds) - 1):
            
            s += line[bounds[i]:bounds[i+1]] + ','

        print(s)


if __name__ == "__main__":
    main()