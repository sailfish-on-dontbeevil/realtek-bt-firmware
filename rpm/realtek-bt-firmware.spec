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
cp %{SOURCE1} $RPM_BUILD_ROOT/lib/firmware/rtl_bt/
cp %{SOURCE2} $RPM_BUILD_ROOT/lib/firmware/rtl_bt/
cp %{SOURCE3} $RPM_BUILD_ROOT/lib/firmware/rtl_bt/

%files
/lib/firmware/rtl_bt/
