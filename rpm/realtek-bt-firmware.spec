Name:       realtek-bt-firmware
Summary:    BT firmware blobs for PinePhone64
Version:    1.0
Release:    0
Group:      System/Firmware
License:    Redistributable
URL:        https://github.com/anarsoul/rtl8723bt-firmware
Source0:     %{name}-%{version}.tar.bz2
Source1:    rtl8723bs_config.bin
Source2:    rtl8723cs_xx_config.bin
Source3:    rtl8723cs_xx_fw.bin
Source4:    rtw8703b_fw.bin
Source5:    rtw8703b_wow_fw.bin

%description
This package contains the realtek BT formware for
PinePhone.

%prep
ls -lhR .
%setup -q -n %{name}-%{version}

%build
ls -lR .

%install
pwd
ls -lR .
mkdir -p $RPM_BUILD_ROOT/lib/firmware/rtl_bt/
mkdir -p $RPM_BUILD_ROOT/lib/firmware/rtw88/
cp %{SOURCE1} $RPM_BUILD_ROOT/lib/firmware/rtl_bt/
cp %{SOURCE2} $RPM_BUILD_ROOT/lib/firmware/rtl_bt/
ln -s /lib/firmware/rtl_bt/%{SOURCE2} $RPM_BUILD_ROOT/lib/firmware/rtl_bt/rtl8723cs_xx_config-pinephone.bin
cp %{SOURCE3} $RPM_BUILD_ROOT/lib/firmware/rtl_bt/
cp %{SOURCE4} $RPM_BUILD_ROOT/lib/firmware/rtw88/
cp %{SOURCE5} $RPM_BUILD_ROOT/lib/firmware/rtw88/

%files
/lib/firmware/rtl_bt/
/lib/firmware/rtw88/
