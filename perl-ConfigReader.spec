%define		pdir	Config
%define		pnam	Reader
%include	/usr/lib/rpm/macros.perl
Summary:	ConfigReader - read directives from a configuration file
Summary(pl.UTF-8):	ConfigReader - odczyt dyrektywy z pliku konfiguracyjnego
Name:		perl-ConfigReader
Version:	0.5
Release:	6
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	469a77797740e7dd70ab902d0ac8081d
URL:		http://search.cpan.org/dist/Config-Reader/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ConfigReader is a set of classes for reading configuration files. The
programmer can easily specify the directives to be read, as well as
their default values and a parsing function or method to use. A lot of
work went into error handling.

%description -l pl.UTF-8
ConfigReader jest zbiorem klas, służących do czytania plików
konfiguracyjnych. Programista może w prosty sposób wskazać dyrektywy
do przeczytania, ich domyślne wartości i funkcję, którą należy
zastosować do sprawdzania składni.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
touch Makefile.PL
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"ConfigReader::Spec");' \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/ConfigReader
%{perl_vendorlib}/ConfigReader/*.pm
%{_mandir}/man3/*
