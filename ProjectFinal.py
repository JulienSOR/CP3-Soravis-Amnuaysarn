import yfinance as yf
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
import matplotlib.pyplot as plt
import numpy as np
''' ขออนุญาติจริงๆครับ อาจจะไม่ได้ใช้ API หรือ module ตามคลิปที่สอน เช่น tkinter 
โดยผมใช้เป็นPyQt แทน เนื่องจากส่วนตัวคิดว่ามีลูกเล่นที่ละเอียดมากกว่าตัว module tkinter
'''
class Infowindow(QWidget):
    def __init__(self,parent,data_finance):
        super().__init__()
        self.parent = parent # ตัวแปรใช้อ้างอิงถึงคลาสแม่(parent)
        self.data_finance = data_finance
        self.setWindowTitle("ดูข้อมูลหุ้น")
        # layout
        vbox_main = QVBoxLayout()
        self.setLayout(vbox_main)

        vbox = QVBoxLayout()
        self.setLayout(vbox)
        grid = QGridLayout()
        self.setLayout(grid)
        # add sublayout to mainlayout
        vbox_main.addLayout(vbox)
        vbox_main.addLayout(grid)
        # widget

        self.table = QTableWidget()
        vbox.addWidget(self.table)

        self.updateTable()

        self.parent.labelgridDisplay("ข้อมูลต้องการพล็อต",grid,0,0)
        self.parent.labelgridDisplay("ลักษณะกราฟ",grid,1,0)
        self.parent.labelgridDisplay("แสดงชื่อไฟล์ PNG export", grid, 2, 0)
        self.data = self.data_finance.index
        self.dataplot = self.parent.comboboxGridDisplay(self.data,grid,0,1,self.getdataplot)
        self.attribute_plot = ["Line","Bar"]
        self.typeplot = self.parent.comboboxGridDisplay(self.attribute_plot, grid, 1, 1,self.gettypeplot)

        self.textedit = QLineEdit()
        grid.addWidget(self.textedit,2,1)

        self.btn1 = QPushButton("SAVE & PLOT")
        grid.addWidget(self.btn1, 2, 2)
        self.btn1.clicked.connect(self.plot)

    def plot(self):
        namePlot = self.getdataplot() # ชื่อแถวที่จะพล็อต
        typePlot = self.gettypeplot()
        saveFile = self.browseFileDialog() # ชื่อไฟล์ที่ต้องการ save
        y = self.data_finance.loc[namePlot].tolist()
        x = self.data_finance.columns.strftime("%Y-%m-%d").tolist()
        x = [str(value) if value != 'N/A' else np.nan for value in x]
        y = [float(value) if value != 'N/A' else np.nan for value in y]
        if typePlot == "Line":
            plt.plot(x,y)
        elif typePlot == "Bar":
            plt.bar(x,y)
        plt.show()
        plt.savefig(saveFile)
    def browseFileDialog(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "PNG Files (*.png);;All Files (*.*)")
        if file_path:
            self.textedit.setText(file_path)
        print(file_path)
        return file_path
    def getdataplot(self): # แถวที่ต้องการพล็อต
        index = self.dataplot.currentIndex()
        print(self.data[index-1])
        return self.data[index-1]
    def gettypeplot(self):
        index = self.typeplot.currentIndex()
        print(self.attribute_plot[index-1])
        return self.attribute_plot[index-1]
    def updateTable(self):

        self.table.setRowCount(len(self.data_finance))
        self.table.setColumnCount(len(self.data_finance.columns) + 1)

        index_name = self.data_finance.index.name if self.data_finance.index.name else "Info"
        headers = [index_name] + self.data_finance.columns.strftime("%Y-%m-%d").tolist()
        self.table.setHorizontalHeaderLabels(headers)
        for i, (index, row) in enumerate(self.data_finance.iterrows()):
            self.table.setItem(i, 0, QTableWidgetItem(str(index)))
            for j, value in enumerate(row):
                self.table.setItem(i, j+1, QTableWidgetItem(str(value)))
    def closeEvent(self, event):
        self.parent.setWindowToNone('infoshare')
        event.accept()
class Pricewindow(QWidget):
    def __init__(self,parent,data_price):
        super().__init__()
        self.parent = parent # ตัวแปรใช้อ้างอิงถึงคลาสแม่(parent)
        self.data_price = data_price
        self.setWindowTitle("ดูราคา")

        # layout
        vbox_main = QVBoxLayout()
        self.setLayout(vbox_main)
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        grid = QGridLayout()
        self.setLayout(grid)
        # add sublayout to mainlayout
        vbox_main.addLayout(vbox)
        vbox_main.addLayout(grid)
        # widget
        self.table = QTableWidget()
        vbox.addWidget(self.table)
        self.updateTable()

        self.parent.labelgridDisplay("ข้อมูลต้องการพล็อต", grid, 0, 0)
        self.parent.labelgridDisplay("ลักษณะกราฟ", grid, 1, 0)
        self.parent.labelgridDisplay("ชื่อไฟล์ export", grid, 2, 0)
        self.data = self.data_price.columns

        self.dataplot = self.parent.comboboxGridDisplay(self.data, grid, 0, 1,self.getdataplot)

        self.attribute_plot = ["Line","Bar","Scatter"]
        self.typeplot = self.parent.comboboxGridDisplay(self.attribute_plot, grid, 1, 1,self.gettypeplot)

        self.textedit = QLineEdit()
        grid.addWidget(self.textedit, 2, 1)

        self.btn1 = QPushButton("SAVE & PLOT")
        grid.addWidget(self.btn1, 2, 2)
        self.btn1.clicked.connect(self.plot)
    def plot(self):
        namePlot = self.getdataplot() # ชื่อคอลัมป์ที่จะพล็อต
        typePlot = self.gettypeplot()
        saveFile = self.browseFileDialog() # ชื่อไฟล์ที่ต้องการ save
        y = self.data_price[namePlot].tolist()
        x = self.data_price.index.strftime("%Y-%m-%d").tolist()
        if typePlot == "Line":
            plt.plot(x,y)
        elif typePlot == "Bar":
            plt.bar(x,y)
        elif typePlot == "Scatter":
            plt.scatter(x,y)
        plt.show()
        plt.savefig(saveFile)
    def browseFileDialog(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "PNG Files (*.png);;All Files (*.*)")
        if file_path:
            self.textedit.setText(file_path)
        print(file_path)
        return file_path
    def getdataplot(self):
        index = self.dataplot.currentIndex()
        print(self.data[index-1])
        return self.data[index-1]
    def gettypeplot(self):
        index = self.typeplot.currentIndex()
        print(self.attribute_plot[index-1])
        return self.attribute_plot[index-1]
    def updateTable(self):
        self.table.setRowCount(len(self.data_price))
        self.table.setColumnCount(len(self.data_price.columns)+1)

        headers = ["Date"] + list(self.data_price.columns)
        self.table.setHorizontalHeaderLabels(headers)
        for i, (index, row) in enumerate(self.data_price.iterrows()):
            self.table.setItem(i, 0, QTableWidgetItem(str(index)))
            for j, value in enumerate(row):
                self.table.setItem(i, j+1, QTableWidgetItem(str(value)))
    def closeEvent(self, event):
        self.parent.setWindowToNone('priceshare')
        event.accept()
class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("โปรแกรมดูราคาและข้อมูลหุ้น")
        # Layout
        vbox_main = QVBoxLayout()
        self.setLayout(vbox_main)
        grid = QGridLayout(self)
        hbox = QHBoxLayout(self)
        # add sub layout to main layout
        vbox_main.addLayout(grid)
        vbox_main.addLayout(hbox)
        # add widget to layout
        self.labelgridDisplay("ชื่อหุ้น",grid,0,0)
        self.labelgridDisplay("เวลาเริ่มต้น",grid,1,0)
        self.labelgridDisplay("ถึง", grid, 1, 2)
        self.labelgridDisplay("interval", grid, 2, 0)

        self.shares = ['EE.bk', 'GFPT.bk', 'LEE.bk', 'MAX.bk', 'NER.bk', 'PPPM.bk',
                       'STA.bk', 'TEGH.bk', 'TFM.bk', 'TRUBB.bk', 'TWPC.bk', 'UPOIC.bk',
                       'UVAN.bk', 'VPO.bk', 'AAI.bk', 'APURE.bk', 'ASIAN.bk', 'BR.bk',
                       'BRR.bk', 'BTG.bk', 'CBG.bk', 'CFRESH.bk', 'CH.bk', 'CHOTI.bk',
                       'CM.bk', 'CPF.bk', 'CPI.bk', 'F&D.bk', 'GLOCON.bk', 'HTC.bk',
                       'ICHI.bk', 'JDF.bk', 'KBS.bk', 'KSL.bk', 'KTIS.bk', 'LST.bk',
                       'M.bk', 'MALEE.bk', 'MINT.bk', 'NRF.bk', 'NSL.bk', 'OISHI.bk',
                       'OSP.bk', 'PB.bk', 'PLUS.bk', 'PM.bk', 'PRG.bk', 'RBF.bk',
                       'SAPPE.bk', 'SAUCE.bk', 'SFP.bk', 'SNNP.bk', 'SNP.bk', 'SORKON.bk',
                       'SSC.bk', 'SSF.bk', 'SST.bk', 'SUN.bk', 'TC.bk', 'TFG.bk',
                       'TFMAMA.bk', 'TIPCO.bk', 'TKN.bk', 'TU.bk', 'TVO.bk', 'W.bk',
                       'ZEN.bk', 'AFC.bk', 'BTNC.bk', 'CPH.bk', 'CPL.bk', 'NC.bk',
                       'PAF.bk', 'PDJ.bk', 'PG.bk', 'SABINA.bk', 'SAWANG.bk', 'SUC.bk',
                       'TNL.bk', 'TR.bk', 'TTI.bk', 'TTT.bk', 'UPF.bk', 'WACOAL.bk',
                       'WFX.bk', 'AJA.bk', 'DTCI.bk', 'FANCY.bk', 'FTI.bk', 'KYE.bk',
                       'L&E.bk', 'MODERN.bk', 'OGC.bk', 'ROCK.bk', 'SIAM.bk', 'TCMC.bk',
                       'TSR.bk', 'APCO.bk', 'BIZ.bk', 'DDD.bk', 'JCT.bk', 'KISS.bk',
                       'NV.bk', 'OCC.bk', 'S&J.bk', 'STGT.bk', 'STHAI.bk', 'TNR.bk',
                       'TOG.bk', 'BAY.bk', 'BBL.bk', 'CIMBT.bk', 'KBANK.bk', 'KKP.bk',
                       'KTB.bk', 'LHFG.bk', 'SCB.bk', 'TCAP.bk', 'TISCO.bk', 'TTB.bk',
                       'AEONTS.bk', 'AMANAH.bk', 'ASAP.bk', 'ASK.bk', 'ASP.bk', 'BAM.bk',
                       'BYD.bk', 'CGH.bk', 'CHAYO.bk', 'ECL.bk', 'FNS.bk', 'FSS.bk', 'GBX.bk',
                       'GL.bk', 'HENG.bk', 'IFS.bk', 'JMT.bk', 'KCAR.bk', 'KGI.bk', 'KTC.bk',
                       'MFC.bk', 'MICRO.bk', 'ML.bk', 'MST.bk', 'MTC.bk', 'NCAP.bk', 'PL.bk',
                       'S11.bk', 'SAK.bk', 'SAWAD.bk', 'SCAP.bk', 'TH.bk', 'THANI.bk', 'TIDLOR.bk',
                       'TK.bk', 'TNITY.bk', 'UOBKH.bk', 'XPG.bk', 'AYUD.bk', 'BKI.bk', 'BLA.bk',
                       'BUI.bk', 'CHARAN.bk', 'INSURE.bk', 'KWI.bk', 'MTI.bk', 'NKI.bk', 'NSI.bk',
                       'SMK.bk', 'TGH.bk', 'THRE.bk', 'THREL.bk', 'TIPH.bk', 'TLI.bk', 'TQM.bk',
                       'TSI.bk', 'TVI.bk', '3K-BAT.bk', 'ACG.bk', 'AH.bk', 'CWT.bk', 'EASON.bk',
                       'GYT.bk', 'HFT.bk', 'IHL.bk', 'INGRS.bk', 'IRC.bk', 'PCSGH.bk', 'POLY.bk',
                       'SAT.bk', 'SPG.bk', 'STANLY.bk', 'TKT.bk', 'TNPC.bk', 'TRU.bk', 'TSC.bk',
                       'ALLA.bk', 'ASEFA.bk', 'CPT.bk', 'CRANE.bk', 'CTW.bk', 'FMT.bk', 'HTECH.bk',
                       'KKC.bk', 'PK.bk', 'SNC.bk', 'STARK.bk', 'TCJ.bk', 'TPCS.bk', 'VARO.bk',
                       'UTP.bk', 'BCT.bk', 'CMAN.bk', 'GC.bk', 'GGC.bk', 'GIFT.bk', 'IVL.bk', 'NFC.bk',
                       'PATO.bk', 'PMTA.bk', 'PTTGC.bk', 'SUTHA.bk', 'TCCC.bk', 'TPA.bk', 'UAC.bk', 'UP.bk',
                       'AJ.bk', 'ALUCON.bk', 'BGC.bk', 'CSC.bk', 'NEP.bk', 'PTL.bk', 'SCGP.bk', 'SFLEX.bk',
                       'SITHAI.bk', 'SLP.bk', 'SMPC.bk', 'SPACK.bk', 'TCOAT.bk', 'TFI.bk', 'THIP.bk', 'TMD.bk',
                       'TOPP.bk', 'TPAC.bk', 'TPBI.bk', 'TPP.bk', '2S.bk', 'AMC.bk', 'BSBM.bk', 'CEN.bk', 'CITY.bk',
                       'CSP.bk', 'GJS.bk', 'GSTEEL.bk', 'INOX.bk', 'LHK.bk', 'MCS.bk', 'MILL.bk', 'PAP.bk', 'PERM.bk',
                       'SAM.bk', 'SMIT.bk', 'SSSC.bk', 'TGPRO.bk', 'THE.bk', 'TMT.bk', 'TSTH.bk', 'TWP.bk', 'TYCN.bk',
                       'CCP.bk', 'COTTO.bk', 'DCC.bk', 'DCON.bk', 'DRT.bk', 'EPG.bk', 'GEL.bk', 'PPP.bk', 'Q-CON.bk',
                       'SCC.bk', 'SCCC.bk', 'SCP.bk', 'SKN.bk', 'STECH.bk', 'TASCO.bk', 'TOA.bk', 'TPIPL.bk', 'UMI.bk',
                       'VNG.bk', 'WIIK.bk', 'A.bk', 'AMATA.bk', 'AMATAV.bk', 'ANAN.bk', 'AP.bk', 'APEX.bk', 'AQ.bk',
                       'ASW.bk', 'AWC.bk', 'BLAND.bk', 'BRI.bk', 'BROCK.bk', 'CGD.bk', 'CI.bk', 'CMC.bk', 'CPN.bk',
                       'ESTAR.bk', 'EVER.bk', 'FPT.bk', 'GLAND.bk', 'J.bk', 'JCK.bk', 'KC.bk', 'LALIN.bk', 'LH.bk',
                       'LPN.bk', 'MBK.bk', 'MJD.bk', 'MK.bk', 'NCH.bk', 'NNCL.bk', 'NOBLE.bk', 'NUSA.bk', 'NVD.bk',
                       'ORI.bk', 'PACE.bk', 'PEACE.bk', 'PF.bk', 'PIN.bk', 'PLAT.bk', 'POLAR.bk', 'PRECHA.bk', 'PRIN.bk',
                       'PSH.bk', 'QH.bk', 'RICHY.bk', 'RML.bk', 'ROJNA.bk', 'S.bk', 'SA.bk', 'SAMCO.bk', 'SC.bk', 'SENA.bk',
                       'SIRI.bk', 'SPALI.bk', 'U.bk', 'UV.bk', 'WHA.bk', 'WIN.bk', 'AIMCG.bk', 'AIMIRT.bk', 'ALLY.bk',
                       'AMATAR.bk', 'B-WORK.bk', 'BAREIT.bk', 'BKKCP.bk', 'BOFFICE.bk', 'CPNCG.bk', 'CPNREIT.bk',
                       'CPTGF.bk', 'CTARAF.bk', 'DREIT.bk', 'ERWPF.bk', 'FTREIT.bk', 'FUTUREPF.bk', 'GAHREIT.bk',
                       'GROREIT.bk', 'GVREIT.bk', 'HPF.bk', 'IMPACT.bk', 'INETREIT.bk', 'KPNPF.bk', 'KTBSTMR.bk',
                       'LHHOTEL.bk', 'LHPF.bk', 'LHSC.bk', 'LPF.bk', 'LUXF.bk', 'M-II.bk', 'M-PAT.bk', 'M-STOR.bk', 'MIPF.bk',
                       'MIT.bk', 'MJLF.bk', 'MNIT.bk', 'MNIT2.bk', 'MNRF.bk', 'POPF.bk', 'PPF.bk', 'PROSPECT.bk', 'QHHR.bk',
                       'QHOP.bk', 'QHPF.bk', 'SHREIT.bk', 'SIRIP.bk', 'SPRIME.bk', 'SRIPANWA.bk', 'SSPF.bk', 'SSTRT.bk', 'TIF1.bk',
                       'TLHPF.bk', 'TNPF.bk', 'TPRIME.bk', 'TTLPF.bk', 'TU-PF.bk', 'URBNPF.bk', 'WHABT.bk', 'WHAIR.bk', 'WHART.bk',
                       'APCS.bk', 'BJCHI.bk', 'BKD.bk', 'CIVIL.bk', 'CK.bk', 'CNT.bk', 'EMC.bk', 'ITD.bk', 'NWR.bk', 'PLE.bk',
                       'PREB.bk', 'PYLON.bk', 'RT.bk', 'SEAFCO.bk', 'SQ.bk', 'SRICHA.bk', 'STEC.bk', 'STI.bk',
                       'STPI.bk', 'SYNTEC.bk', 'TEAMG.bk', 'TEKA.bk', 'TPOLY.bk', 'TRC.bk', 'TRITN.bk', 'TTCL.bk',
                       'UNIQ.bk', 'WGE.bk', '7UP.bk', 'ABPIF.bk', 'ACC.bk', 'ACE.bk', 'AGE.bk', 'AI.bk', 'AIE.bk',
                       'AKR.bk', 'BAFS.bk', 'BANPU.bk', 'BBGI.bk', 'BCP.bk', 'BCPG.bk', 'BGRIM.bk', 'BPP.bk',
                       'BRRGIF.bk', 'CKP.bk', 'CV.bk', 'DEMCO.bk', 'EA.bk', 'EASTW.bk', 'EGATIF.bk', 'EGCO.bk',
                       'EP.bk', 'ESSO.bk', 'ETC.bk', 'GPSC.bk', 'GREEN.bk', 'GULF.bk', 'GUNKUL.bk', 'IFEC.bk',
                       'IRPC.bk', 'JR.bk', 'KBSPIF.bk', 'LANNA.bk', 'MDX.bk', 'NOVA.bk', 'OR.bk', 'PCC.bk',
                       'PRIME.bk', 'PTG.bk', 'PTT.bk', 'PTTEP.bk', 'QTC.bk', 'RATCH.bk', 'RPC.bk', 'SCG.bk',
                       'SCI.bk', 'SCN.bk', 'SGP.bk', 'SKE.bk', 'SOLAR.bk', 'SPCG.bk', 'SPRC.bk', 'SSP.bk',
                       'SUPER.bk', 'SUPEREIF.bk', 'SUSCO.bk', 'TAE.bk', 'TCC.bk', 'TGE.bk', 'TOP.bk', 'TPIPP.bk',
                       'TSE.bk', 'TTW.bk', 'UBE.bk', 'WHAUP.bk', 'WP.bk', 'THL.bk', 'B52.bk', 'BEAUTY.bk', 'BIG.bk',
                       'BJC.bk', 'COM7.bk', 'CPALL.bk', 'CPW.bk', 'CRC.bk', 'CSS.bk', 'DOHOME.bk', 'FN.bk', 'FTE.bk',
                       'GLOBAL.bk', 'HMPRO.bk', 'ICC.bk', 'ILM.bk', 'IT.bk', 'KAMART.bk', 'LOXLEY.bk', 'MAKRO.bk',
                       'MC.bk', 'MEGA.bk', 'MIDA.bk', 'RS.bk', 'RSP.bk', 'SABUY.bk', 'SCM.bk', 'SINGER.bk', 'SPC.bk',
                       'SPI.bk', 'SVT.bk', 'AHC.bk', 'BCH.bk', 'BDMS.bk', 'BH.bk', 'CHG.bk', 'CMR.bk', 'EKH.bk',
                       'KDH.bk', 'LPH.bk', 'M-CHAI.bk', 'NEW.bk', 'NTV.bk', 'PR9.bk', 'PRINC.bk', 'RAM.bk', 'RJH.bk',
                       'RPH.bk', 'SKR.bk', 'SVH.bk', 'THG.bk', 'VIBHA.bk', 'VIH.bk', 'WPH.bk', 'AMARIN.bk', 'AQUA.bk',
                       'AS.bk', 'BEC.bk', 'FE.bk', 'GPI.bk', 'GRAMMY.bk', 'JKN.bk', 'MACO.bk', 'MAJOR.bk', 'MATCH.bk',
                       'MATI.bk', 'MCOT.bk', 'MONO.bk', 'MPIC.bk', 'NATION.bk', 'ONEE.bk', 'PLANB.bk', 'POST.bk',
                       'PRAKIT.bk', 'PTECH.bk', 'SE-ED.bk', 'TKS.bk', 'VGI.bk', 'WAVE.bk', 'WORK.bk', 'BWG.bk',
                       'GENCO.bk', 'PRO.bk', 'SISB.bk', 'SO.bk', 'ASIA.bk', 'BEYOND.bk', 'CENTEL.bk', 'CSR.bk',
                       'DUSIT.bk', 'ERW.bk', 'GRAND.bk', 'LRH.bk', 'MANRIN.bk', 'OHTL.bk', 'ROH.bk', 'SHANG.bk',
                       'SHR.bk', 'VRANDA.bk', 'AAV.bk', 'AOT.bk', 'ASIMAR.bk', 'B.bk', 'BA.bk', 'BEM.bk', 'BIOTEC.bk',
                       'BTS.bk', 'BTSGIF.bk', 'DMT.bk', 'III.bk', 'JWD.bk', 'KEX.bk', 'KIAT.bk', 'KWC.bk', 'MENA.bk',
                       'NOK.bk', 'NYT.bk', 'PORT.bk', 'PRM.bk', 'PSL.bk', 'RCL.bk', 'TFFIF.bk', 'THAI.bk', 'TSTE.bk',
                       'TTA.bk', 'WICE.bk', 'CCET.bk', 'DELTA.bk', 'HANA.bk', 'KCE.bk', 'METCO.bk', 'NEX.bk', 'SMT.bk',
                       'SVI.bk', 'TEAM.bk', 'ADVANC.bk', 'AIT.bk', 'ALT.bk', 'AMR.bk', 'BLISS.bk', 'DIF.bk', 'DTAC.bk',
                       'FORTH.bk', 'HUMAN.bk', 'ILINK.bk', 'INET.bk', 'INSET.bk', 'INTUCH.bk', 'ITEL.bk', 'JAS.bk',
                       'JASIF.bk', 'JMART.bk', 'JTS.bk', 'MFEC.bk', 'MSC.bk', 'PT.bk', 'SAMART.bk', 'SAMTEL.bk',
                       'SDC.bk', 'SIS.bk', 'SKY.bk', 'SVOA.bk', 'SYMC.bk', 'SYNEX.bk', 'THCOM.bk', 'TKC.bk', 'TRUE.bk',
                       'TWZ.bk']
        self.share_combobox = self.comboboxGridDisplay(self.shares,grid,0,1,self.getshare)
        self.intervals = ["1m","1h","1d","1mo"]
        self.interval_combobox = self.comboboxGridDisplay(self.intervals, grid, 2, 1,self.getinterval)

        self.date_start = self.dateeditGridDisplay(grid,1,1,self.dateStart)
        self.date_end = self.dateeditGridDisplay(grid, 1, 3,self.dateEnd)

        self.infoshare = None
        self.priceshare = None
        btn1 = QPushButton("ดูข้อมูล")
        hbox.addWidget(btn1)
        btn2 = QPushButton("ดูราคา")
        hbox.addWidget(btn2)
        # signal
        btn1.clicked.connect(self.displayInfoWindow)
        btn2.clicked.connect(self.displayPriceWindow)
    def displayInfoWindow(self):
        if self.infoshare is None:
            data = self.financeData()

            self.infoshare = Infowindow(self,data)
            self.infoshare.show()

    def displayPriceWindow(self):
        if self.priceshare is None:
            data = self.historyPrice()
            self.priceshare = Pricewindow(self,data) # ใส่ self เพื่อกำหนดให้หน้าต่าง Pricewindow เป็นหน้าต่างลูกของ Mainwindow
            self.priceshare.show()

    def setWindowToNone(self, window_name):
        if window_name == 'infoshare':
            self.infoshare = None
        elif window_name == 'priceshare':
            self.priceshare = None
    def labelgridDisplay(self,text,layout,row,column):
        lb = QLabel(text)
        layout.addWidget(lb,row,column)
    def comboboxGridDisplay(self,data,layout,row,column,func):
        combobox = QComboBox()
        combobox.addItem("")
        combobox.addItems(data)
        layout.addWidget(combobox,row,column)
        combobox.currentIndexChanged.connect(func)
        return combobox
    def getshare(self):
        index = self.share_combobox.currentIndex()
        print(self.shares[index-1])
        return self.shares[index-1]
    def getinterval(self):
        index = self.interval_combobox.currentIndex()
        print(self.intervals[index-1])
        return self.intervals[index-1]

    def dateeditGridDisplay(self,layout,row,column,func):
        date_edit = QDateEdit()
        date_edit.setCalendarPopup(True) # เปิดปฏิทินแบบป๊อปอัป
        date_edit.setDate(QDate.currentDate()) # ตั้งค่าวันที่เริ่มต้นเป็นวันที่ปัจจุบัน
        layout.addWidget(date_edit, row, column)
        date_edit.dateChanged.connect(func)
        return date_edit

    def dateStart(self):
        selected_date = self.date_start.date()
        formatted_date = selected_date.toString("yyyy-MM-dd")
        print(formatted_date)
        return formatted_date
    def dateEnd(self):
        selected_date = self.date_end.date()
        formatted_date = selected_date.toString("yyyy-MM-dd")
        print(formatted_date)
        return formatted_date
    def financeData(self):
        share_Name = self.getshare()
        shareTriker = yf.Ticker(share_Name)
        finance_data = shareTriker.financials
        finance_data.index.name = "Info"
        finance_data.fillna("N/A",inplace=True)
        finance_data.dropna(inplace=True)
        print(finance_data)
        return finance_data

    def historyPrice(self):
        start_date = self.dateStart()
        end_date = self.dateEnd()
        share_Name =self.getshare()
        interval = self.getinterval()
        shareTriker = yf.Ticker(share_Name)
        shareTriker_df = shareTriker.history(interval=interval,start=start_date,end=end_date)
        shareTriker_df.fillna("N/A",inplace=True)
        print(shareTriker_df)
        return shareTriker_df
# Run Program
app = QCoreApplication.instance()
if app is None:
    app = QApplication([])

window = Mainwindow()
window.show()
app.exec()